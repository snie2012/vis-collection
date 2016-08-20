function backToTreeLayout() {
  d3.select('svg').style('background-color', '')
  d3.select('iframe').style('display', 'none');
  canvas.remove();
  setCanvas();
  update(root);
}

function updateIframe(src) {
    var IFrame = document.getElementsByTagName('iframe')[0];
    
    IFrame.src = src;
    IFrame.onload = function() {
        var frameBody = IFrame.contentDocument.body;
        IFrame.style['margin-left'] =  margin.left;
        //IFrame.style['margin-right'] =  20;
        IFrame.style.width = window.innerWidth / 1.2;
        IFrame.style.height = Math.max(frameBody.scrollHeight, window.innerHeight);
        IFrame.style['background-color'] = 'blueviolet';
        IFrame.style['border-radius'] = '36px';
        IFrame.style.display = 'block';
    }
}


function transitToNav(node) {
  var selectedNode = canvas.selectAll('g.node')
    .filter(function(d) {
      if (node === d) return true;
    });

  selectedNode.select('circle')
    .style('fill', 'pink');

  var toRemove = canvas.selectAll('g.node, path.link')
    .filter(function(d) {
      if (node.parent.children.indexOf(d) < 0 || (d.children || d._children)) {
        return true;
      }
    });
  var count = 0;
  var len = toRemove[0].length;

  toRemove.transition()
    .duration(duration)
    .style('opacity', 0)
    .remove()
    .each('end', function() {
      count++;
      if (count === len) {
        var toTransit = canvas.selectAll('g.node');
        count = 0;
        len = toTransit[0].length;

        toTransit.transition()
          .duration(200)
          .delay(function(d, i) {return i * 100})
          .attr("transform", function(d, i) { return "translate(" +  (window.innerWidth / 5 + i * circleSize * 2.2) + "," + circleSize + ")"; })
          .each('end', function() {
            count++;

            // After all transition is finished
            if (count === len) {
                toTransit.on('click', null);

                var backButtom = canvas.append('g')
                  .attr('id', 'back-buttom')
                  .attr("transform", function(d, i) { return "translate(" +  0 + "," + circleSize / 2 + ")"; })
                  .on('click', backToTreeLayout);

                backButtom.append('circle')
                  .attr('r', circleSize / 2)
                  .attr('opacity', 0)
                  .transition()
                  .duration(duration)
                  .attr('opacity', 1);

                backButtom.append('text')
                  .text('back')
                  .attr('text-anchor', 'middle')
                  .attr('dy', ".35em")
                  .attr('opacity', 0)
                  .transition()
                  .duration(duration)
                  .attr('opacity', 1)
                  .each('end', function() {
                    d3.select('svg')
                      .attr('height', circleSize * 3);
                      
                    updateIframe(node.src);

                    toTransit.on('click', function(d) {

                      // if click on the activated tab, do nothing and return
                      if (d3.select(this).select('circle').style('fill') == 'rgb(255, 192, 203)') {
                        return;
                      }


                      d3.selectAll('g.node')
                        .filter(function(data) {
                          if (data !== d) return true;
                        })
                        .select('circle')
                        .style('fill', 'rgb(256, 256, 256)');

                      d3.selectAll('g.node')
                        .filter(function(data) {
                          if (data === d) return true;
                        })
                        .select('circle')
                        .style('fill', 'rgb(255, 192, 203)');

                      updateIframe(d.src);
                    })
                });
              }
          });
      }
    });
}







