var canvas;
var root;

var datapath;
var colorPallete;

var margin;
var width;
var height;

var circleSize;
var idCount;
var duration;
var tree;
var diagonal;

function init() {
    datapath = "/en/homepage/json/";
    colorPallete = ['#ff6666', '#6677ff', '#339933', '#999966'];

    margin = {top: 20, right: 120, bottom: 20, left: 60};
    width = window.innerWidth - margin.right - margin.left;
    height = window.innerHeight - margin.top - margin.bottom;

    circleSize = 45;

    idCount = 0;
    duration = 500;

    tree = d3.layout.tree()
        .size([height, width]);

    diagonal = d3.svg.diagonal()
        .projection(function(d) { return [d.y, d.x]; });

}

function setCanvas() {
    canvas = d3.select("svg")
        .attr("width", width + margin.right + margin.left)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");   
}

/* 
Color tree data structure with the provided pallete.
Arg: root node of tree; color pallete
Return: none
*/
function colorTree(rNode, pallete) {
  rNode.color = "white";
  for (var i = 0; i < rNode.children.length; i++) {
    rNode.children[i].color = pallete[i];
    colorSubTree(rNode.children[i], pallete[i]);
  }
}

function colorSubTree(n, c) {
  if (n.children) {
    n.children.forEach(function(e) {
      e.color = c;
      colorSubTree(e);
    });
  } else {
    return;
  }
}

function collapse(d) {
  if (d.children) {
    d._children = d.children;
    d._children.forEach(collapse);
    d.children = null;
  }
}


/* Position the root node when the page is loaded at the beginning
*/
function initialDisplay() {
  var node = canvas.selectAll("g.node")
      .data(tree.nodes(root));

  var rootEnter = node.enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + width / 2 + "," + height / 2.4 + ")"; })
      .on('click', function() {
        update(root);
        setTimeout(function(){
          click(root);
          rootEnter.on('click', click);
        }, duration * 1.1);
      });

  rootEnter.append("circle")
      .attr("r", 0)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  rootEnter.append("text")
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .text(function(d) { return d.name; })
      .style("fill-opacity", 0)
      .style('font-size', '1em');

  var rootUpdate = node.transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + width / 2 + "," + height / 2.4 + ")"; });

  rootUpdate.select("circle")
      .attr("r", circleSize * 2)
      .style("stroke", function(d) {return d.color;})
      .style("fill","lightsteelblue");

  rootUpdate.select("text")
      .style("fill-opacity", 1);
}


/*
Called in the click functin. Every time a click evernt happens, update is called once.
*/
function update(source) {
  // Compute the new tree layout.
  var nodes = tree.nodes(root),
      links = tree.links(nodes);

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = (d.depth + 1) * width / 5;});

  // Update the nodes…
  var node = canvas.selectAll("g.node")
      .data(nodes, function(d) { return d.id || (d.id = ++idCount); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
      .on("click", click);

  nodeEnter.append("circle")
      .attr("r", 0);

  nodeEnter.append("text")
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .text(function(d) { return d.name; })
      .style("fill-opacity", 0);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

  nodeUpdate.select("circle")
      .attr("r", circleSize)
      .style("stroke", function(d) {return d.color;})
      .style('stroke-width', function(d) {
        return (d.children || d._children) ? 5 : 0;
      })
      .style("fill", function(d) { return d._children ? "lightsteelblue" : d.children ? "#fff" : "#fff";});

  nodeUpdate.select("text")
      .style("fill-opacity", 1);

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + d.parent.y + "," + d.parent.x + ")"; })
      .remove();

  nodeExit.select("circle")
      .attr("r", 0);

  nodeExit.select("text")
      .style("fill-opacity", 0);

  // Update the links…
  var link = canvas.selectAll("path.link")
      .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
      .attr("class", "link")
      .attr("d", function(d) {
        var o = {x: source.x0, y: source.y0};
        return diagonal({source: o, target: o});
      });

  // Transition links to their new position.
  link.transition()
      .duration(duration)
      .attr("d", diagonal)
      .style("stroke", function(d) {return d.target.color});

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
      .duration(duration)
      .attr("d", function(d) {
        var o = {x: d.source.x, y: d.source.y};
        return diagonal({source: o, target: o});
      })
      .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
    d.x0 = d.x;
    d.y0 = d.y;
  });
}


// Toggle children on click.
function click(d) {
  if (d.children) {
    d._children = d.children;
    d.children = null;
  } else {
    d.children = d._children;
    d._children = null;

    // collapse all the other nodes on the same level
    if (d.parent) {
      d.parent.children.forEach(function(e) {
        if (e !== d && e.children) {
          e._children = e.children;
          e.children = null;
        }
      })
    }
  }

  if (!d.children && !d._children) {
    transitToNav(d);
  } else {
    update(d);
  }
}
 

init();
d3.json(datapath, function(error, d) {    
    if (error) throw error;

    setCanvas();
    colorTree(d, colorPallete);

    root = d;
    root.x0 = height / 2;
    root.y0 = 0;

    collapse(root);
    initialDisplay();
});








