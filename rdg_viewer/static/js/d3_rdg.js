var margin = { top: 20, right: 90, bottom: 30, left: 90 },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var svg = d3.select("#tree")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var data = {{ tree_data|safe }};

var tree = d3.tree().size([height, width]);

var root = d3.hierarchy(data);

tree(root);

svg.selectAll(".link")
  .data(root.descendants().slice(1))
  .enter().append("path")
    .attr("class", "link")
    .attr("d", function(d) {
      return "M" + d.y + "," + d.x
          + "C" + (d.parent.y + 100) + "," + d.x
          + " " + (d.parent.y + 100) + "," + d.parent.x
          + " " + d.parent.y + "," + d.parent.x;
    });

var node = svg.selectAll(".node")
  .data(root.descendants())
  .enter().append("g")
    .attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
    .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

node.filter(function(d) { return !d.children; })
  .append("circle")
    .attr("r", 2.5);

node.append("text")
  .attr("dy", 3)
  .attr("x", function(d) { return d.children ? -8 : 8; })
  .style("text-anchor", function(d) { return d.children ? "end" : "start"; })
  .text(function(d) { return d.data.name; });
