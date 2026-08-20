---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/CreatingChartsandGraphs/CreatingChartsandGraphs.html
archived_at: '2026-07-15T05:21:05.889771Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Animating%20the%20Canvas.md)[Previous](Advanced%20Compositing.md)

# Creating Charts and Graphs

It’s easy to generate charts and graphs from data using the `canvas` element. The main difficulty is scaling the data to fit neatly on the page. Graphs are usually presented with the y-axis going up, not down, and the y-coordinates are scaled to fit the data, so you need a way to translate from the data value to a canvas y-coordinate.

There are three common solutions for resolving y-coordinates for graphs and charts:

- Use the transformation matrix to flip and scale the canvas’s y-axis.
- Write a routine that calculates a y-coordinate from the data.
- Use a data visualization JavaScript library.

This chapter shows you how to use the transformation matrix for graphing and how to calculate a y-coordinate for a data point on a graph. If you’d prefer to use a JavaScript library, a web search for “canvas JavaScript libraries” or “canvas JavaScript libraries data visualization” will turn up a current list of libraries.

This chapter shows you how to create data plots, bar graphs, and pie charts.

A graph or chart normally contains lines or bars plotted against a grid. There is often text or artwork on the chart as well, including a vertical scale along the left edge.

You can use a single `canvas` element for the whole chart, or you can use a canvas element just as a grid for the data, surrounding the grid with text and artwork using HTML and CSS, or positioning a `canvas` element inside of another `canvas` element using CSS.

If you are using a `canvas` element primarily as a grid, the easy way to fit your data to the grid is to use the transformation matrix. The transformation matrix can flip the y-axis, scale the y-axis so the vertical display area equals your data range, and translate the y-axis zero point to the zero point for your data. Then your data value _is_ the y-coordinate.

If you include text or art on the canvas, you probably don’t want to transform the text or art using the matrix—it would be upside down and stretched vertically. You can either render the art or text before you change the transformation matrix, or you can save the context, graph the data, restore the context, and draw your text or art.

If you draw art or text on the canvas, positioned relative to the data, you need to use JavaScript to calculate the appropriate y-coordinates.

If your data needs to be plotted against a log scale instead of a linear scale, the transformation matrix won’t be much help—the matrix is for linear transforms. You need to use JavaScript to calculate the proper y-coordinates for your data.

To scale the y-axis to fit your data using the transformation matrix, you need to know the minimum and maximum data values of your grid and the size of any header or footer area of the canvas that isn’t used for graphing.

Listing 10-1 performs the transformation to scale the y-axis and position the zero point correctly, once you set the variables.

__Listing 10-1__  Scaling by matrix

```
var can, ctx,
    maxVal, minVal,
    topMargin, botMargin,
    leftMargin;

function init() {
    can = document.getElementById("can");
    ctx = can.getContext("2d");
}
function transformYAxis() {
    var displayHeight = can.height - topMargin - botMargin;
    var yScalar = displayHeight / (maxVal - minVal);
    //translate to 0, 0 point on data graph
    ctx.translate(leftMargin, can.height + minVal * yScalar);
    // scale canvas to match data graph and flip y-axis
    ctx.scale(1, -1 * yScalar);
}
```


To calculate a canvas y-coordinate from a data value, you need to know the maximum and minimum values on your graph and the height of any header and footer areas of the canvas that won’t be used for graphing.

Listing 10-2 sets the value of `y` from a given data value, once you fill in the maximum and minimum data values and header and footer heights.

__Listing 10-2__  Creating a scaling function

```
// set these four values
var maxVal;
var minVal;
var topMargin;
var botMargin;

var can;
var ctx;
var displayHeight;
var yScalar;
var bottom;
var y;

function init() {
    can = document.getElementById("can");
    ctx = can.getContext("2d");
    displayHeight = can.height - topMargin - botMargin;
    yScalar = displayHeight / (maxVal - minVal);
    bottom = can.height - botMargin;
}
function calcY(value) {
    y = bottom - value * yScalar + yScalar * minVal;
}
```


A data plot is a graph showing your sample data plotted on a grid. If you have more than one data set, the data sets are usually color coded. A sample data plot is shown in Figure 10-1.

__Figure 10-1__  Sample data plot

!

The advantage to using canvas for data plots, instead of drawing them using a graphics tool, is that you can update the artwork just by refreshing the data that it illustrates. This is especially useful for graphing rapidly changing data, real-time data, or user-entered data.

A template for data plots is provided in Listing 10-3. All you have to do is supply the data and set a few variables, such as the minimum and maximum sample values, the number of samples, and any text for the column headers.

The example scales the canvas vertically to the range of sample values, and horizontally to the number of samples. To plot a given sample number _x_, of value _y_, you can simply call `lineTo(x,y)`. The y-axis is scaled to -1 times the scalar, so the y-coordinate increases as you move up the graph.

__Listing 10-3__  Data plot template

```
<html>
<head>
    <title>Plotting Data</title>
    <script type="text/javascript">
        var can, ctx,
            maxVal, minVal,
            xScalar, yScalar,
            numSamples;
        // data sets -- set literally or obtain from an ajax call
        var sanDiego =  [72, 70, 74, 72, 75, 76, 77, 78, 74, 72, 70, 68];
        var kansasCty = [20, 30, 40, 50, 60, 70, 80, 90, 70, 60, 50, 40];
        var buffalo =   [-10, -20, 0, 50, 50, 60, 90, 100, 50, 40, 30, 0];

        function init() {
            // set these values for your data
            numSamples = 12;
            maxVal = 120;
            minVal = -30;
            var stepSize = 10;
            var colHead = 50;
            var rowHead = 50;
            var margin = 5;
            var header = [" ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                          "Sep", "Oct", "Nov", "Dec"]

            can = document.getElementById("can");
            ctx = can.getContext("2d");
            ctx.fillStyle = "black"
            ctx.font = "14pt Helvetica"
            // set vertical scalar to available height / data points
            yScalar = (can.height - colHead - margin) / (maxVal - minVal);
            // set horizontal scalar to available width / number of samples
            xScalar = (can.width - rowHead) / numSamples;

            ctx.strokeStyle="rgba(128, 128, 255, 0.5)"; // light blue lines
            ctx.beginPath();
            // print  column header and draw vertical grid lines
            for (i = 1; i <= numSamples; i++) {
                var x = i * xScalar;
                ctx.fillText(header[i], x, colHead - margin);
                ctx.moveTo(x, colHead);
                ctx.lineTo(x, can.height - margin);
            }
            // print row header and draw horizontal grid lines
            var count = 0;
            for (scale = maxVal; scale >= minVal; scale -= stepSize) {
                var y = colHead + (yScalar * count * stepSize);
                ctx.fillText(scale, margin, y + margin);
                ctx.moveTo(rowHead, y)
                ctx.lineTo(can.width, y)
                count++;
            }
            ctx.stroke();

            // set a color and make one call to plotData()
            // for each data set
            ctx.strokeStyle = "green";
            plotData(sanDiego);
            ctx.strokeStyle = "red";
            plotData(kansasCty);
            ctx.strokeStyle = "purple";
            plotData(buffalo);
        }

        function plotData(dataSet) {
            ctx.beginPath();
            ctx.moveTo(0, dataSet[0]);
            for (i = 1; i < numSamples; i++) {
               ctx.lineTo(i * xScalar, dataSet[i]);
            }
            ctx.stroke();
        }
    </script>
</head>
<body onload="init()">
    <div align="center">
        <h2>Average Temperature By City</h2>
        <canvas id="can" height="400" width="650">
        </canvas>
        <br />
        <!-- identify your data sets -->
        <span style="color:green">San Diego: green</span> &nbsp;
        <span style="color:red">Kansas City: red</span> &nbsp;
        <span style="color:purple">Buffalo: purple</span>
    </div>
</body>
</html>
```


Bar graphs are similar to data plots, but each sample is graphed as a rectangle scaled to the height or width of the sample.

The example in [Listing 10-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjrfvjvona) graphs data as vertical bars with a text label floating over each bar, as shown in Figure 10-2.

__Figure 10-2__  Sample bar graph

!

__Listing 10-4__  Bar graph template

```
<html>
<head>
    <title>Bar Graph</title>
    <script type="text/javascript">
        var can, ctx,
            minVal, maxVal,
            xScalar, yScalar,
            numSamples, y;
        // data sets -- set literally or obtain from an ajax call
        var dataName = [ "Human", "Chimp", "Dolphin", "Cat" ];
        var dataValue = [ 11000, 6200, 5800, 300 ];

        function init() {
            // set these values for your data
            numSamples = 4;
            maxVal = 12000;
            var stepSize = 1000;
            var colHead = 50;
            var rowHead = 60;
            var margin = 10;
            var header = "Millions"
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            ctx.fillStyle = "black"
            yScalar = (can.height - colHead - margin) / (maxVal);
            xScalar = (can.width - rowHead) / (numSamples + 1);
            ctx.strokeStyle = "rgba(128,128,255, 0.5)"; // light blue line
            ctx.beginPath();
            // print  column header
            ctx.font = "14pt Helvetica"
            ctx.fillText(header, 0, colHead - margin);
            // print row header and draw horizontal grid lines
            ctx.font = "12pt Helvetica"
            var count =  0;
            for (scale = maxVal; scale >= 0; scale -= stepSize) {
                y = colHead + (yScalar * count * stepSize);
                ctx.fillText(scale, margin,y + margin);
                ctx.moveTo(rowHead, y)
                ctx.lineTo(can.width, y)
                count++;
            }
            ctx.stroke();
            // label samples
            ctx.font = "14pt Helvetica";
            ctx.textBaseline = "bottom";
            for (i = 0; i < 4; i++) {
                calcY(dataValue[i]);
                ctx.fillText(dataName[i], xScalar * (i + 1), y - margin);
            }
            // set a color and a shadow
            ctx.fillStyle = "green";
            ctx.shadowColor = 'rgba(128,128,128, 0.5)';
            ctx.shadowOffsetX = 20;
            ctx.shadowOffsetY = 1;
            // translate to bottom of graph and scale x,y to match data
            ctx.translate(0, can.height - margin);
            ctx.scale(xScalar, -1 * yScalar);
            // draw bars
            for (i = 0; i < 4; i++) {
                ctx.fillRect(i + 1, 0, 0.5, dataValue[i]);
            }
        }

        function calcY(value) {
            y = can.height - value * yScalar;
        }
    </script>
</head>
<body onload="init()">
    <div align="center">
        <h2>Neurons in Cerebral Cortex</h2>
        <canvas id="can" height="400" width="650">
        </canvas>
    </div>
</body>
</html>
```


You create a pie chart by treating each sample as a wedge of pie—add the samples together to get the size of the pie, determine the proportion of each slice, then render each portion as its part of a circle.

Use the `arc(x,y, radius, startAngle, endAngle)` method to draw the outside of each wedge of the pie.

Set `x,y` to the middle of the canvas, or wherever you want the center of your pie chart.

Set `radius` to no more than half the height or width of the canvas—less if you want to have room for labels.

For the first sample, `startAngle` can be any value—you can start anywhere you like on a circle. For subsequent samples, `startAngle` equals the first `startAngle` plus the `endAngle` of all previous samples.

Set `endAngle` to the fraction of the circle represented by a given sample:

`Math.PI * 2 * sample / total`

Use `lineTo(x,y)` to connect the end of the arc to the center of the pie. Use `closePath()` to connect the center back to the start of the arc and complete the wedge.

Fill the wedge with a color using the `fill()` method. You can outline the shape in another color using the `stroke()` method.

Listing 10-5 draws a pie chart from an array of samples and an array of fill colors.

__Listing 10-5__  Drawing a pie chart

```
var oldAngle = 0;
var midX = can.width /2;
var midY = can.height /2;
var radius = midY;

// do for each sample:
for (i = 0; i < numSamples; i++) {
    // draw wedge
    var portion = dataValue[i] / total;
    var wedge = 2 * Math.PI * portion;
    ctx.beginPath();
    var angle = oldAngle + wedge;
    ctx.arc(midX, midY, radius, oldAngle, angle);
    ctx.lineTo(midX, midY);
    ctx.closePath();
    ctx.fillStyle = fillColor[i];
    ctx.fill();    // fill with wedge color
    ctx.stroke();  // outline in black
    oldAngle += wedge;
}
```

Labeling a pie chart is more art than science, but one approach is to label each sample with text outside the pie, aligned with the center of the wedge.

Positioning the text can be a bit tricky, as it depends on the height and width of the text—you don’t want to run into the pie or off the canvas. Listing 10-6 generates a series of pie charts from a menu of quarterly results and labels the samples as shown in Figure 10-3.

__Figure 10-3__  Sample pie chart

__Listing 10-6__  Pie chart generator

```
<html>
<head>
    <title>Pie Chart</title>
    <script type="text/javascript">
        var can, ctx,
            numSamples,
            xScalar, yScalar,
            radius, quarter;
        // data sets -- set literally or obtain from an ajax call
        var dataName = [ "East", "Midwest", "South", "West" ];
        var q1Value = [ 1200000, 800000, 600000, 3000000 ];
        var q2Value = [ 900000, 900000, 700000, 1800000 ];
        var q3Value = [ 800000, 700000, 600000, 900000 ];
        var fillColor = ["red", "blue", "green", "orange" ];

        function init() {
            // set this value for your data
            numSamples = 4;
            can = document.getElementById("can");
            quarter = document.getElementById("quarter");
            ctx = can.getContext("2d");
            drawPie();
        }

        function drawPie() {
            radius = can.height / 3;
            var midX = can.width / 2;
            var midY = can.height / 2;
            ctx.strokeStyle = "black";
            ctx.font = "18pt Helvetica";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            // get data set
            var dataValue = q1Value;
            if (quarter.value == "q2")
                dataValue = q2Value;
            if (quarter.value == "q3")
                dataValue = q3Value;
            // calculate total value of pie
            var total = 0;
            for (var i = 0; i < numSamples; i++) {
                total += dataValue[i];
            }
            // get ready to draw
            ctx.clearRect(0, 0, can.width, can.height);
            var oldAngle = 0;

            // for each sample
            for (var i = 0; i < numSamples; i++) {
                // draw wedge
                var portion = dataValue[i] / total;
                var wedge = 2 * Math.PI * portion;
                ctx.beginPath();
                var angle = oldAngle + wedge;
                ctx.arc(midX, midY, radius, oldAngle, angle);
                ctx.lineTo(midX, midY);
                ctx.closePath();
                ctx.fillStyle = fillColor[i];
                ctx.fill();    // fill with wedge color
                ctx.stroke();  // outline in black

                // print label
                // set angle to middle of wedge
                var labAngle = oldAngle + wedge / 2;
                // set x, y for label outside center of wedge
                // adjust for fact text is wider than it is tall
                var labX = midX + Math.cos(labAngle) * radius * 1.5;
                var labY = midY + Math.sin(labAngle) * radius * 1.3 - 12;
                // print name and value with black shadow
                ctx.save();
                ctx.shadowColor = "black";
                ctx.shadowOffsetX = 1;
                ctx.shadowOffsetY = -1;
                ctx.fillStyle = fillColor[i];
                ctx.fillText(dataName[i], labX, labY);
                ctx.fillText("$" + dataValue[i], labX, labY + 25);
                ctx.restore();
                // update beginning angle for next wedge
                oldAngle += wedge;
            }
        }
    </script>
</head>
<body onload="init()">
    <div align="center">
        <h2>Sales by Region</h2>
        <canvas id="can" height="400" width="500">
        </canvas>
    </div>
    <br />
    <select id="quarter" onchange="drawPie()" style="font:18pt Helvetica">
        <option value="q1">Q1</option>
        <option value="q2">Q2</option>
        <option value="q3">Q3</option>
    </select>
</body>
</html>
```


Students and the general public find science more interesting when data is presented visually, especially when it changes in response to user input. You can easily add user interaction to a graph by adding a few `<input>` elements to allow users to change variable values.

By adding a value that changes over time, you can often turn a static graph into an animation with a line or two of code. Adding animation and user input makes a graph much more engaging.

The example in [Listing 10-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjrfvjvooi) graphs three sine waves, then graphs the combination of the three waves to illustrate frequency addition, as shown in Figure 10-4.

__Figure 10-4__  Frequency addition

Adding a few buttons makes the graph interactive by allowing the user to change the frequency and phase of the sine waves and see the result.

Adding a global phase variable and incrementing it repeatedly, then redrawing the waves, turns the graphs of the waves into tiny oscilloscopes, transforming a static image into an animation that grabs the eye. For more about animation, see [Animating the Canvas](Animating%20the%20Canvas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjsfvjvomjt).

__Listing 10-7__  Performing interactive frequency addition

```
<!doctype html>
<html>
<head>
    <title>Frequency Addition</title>
    <script type="text/javascript">
        var canvas = [];
        var ctx = [];
        var cHeight = 50;
        var canvasWidth = 180;
        var canvasHeight = 150;
        var aCircle = 2 * Math.PI;
        var ninetyDeg = 0.5 * Math.PI;
        var sixDeg = Math.PI / 30;
        // vertical scale for 3 sine waves above and below x-axis without hitting edges
        var vScale = (canvasHeight / 6) - 2;
        var freq = [];
        var colors = [ "red", "green", "blue", "white" ];
        var phase = [];
        var globalPhase = 0;
        var label = [];

        function init() {
            label[0] = document.getElementById("label0");
            label[1] = document.getElementById("label1");
            label[2] = document.getElementById("label2");
            for (var i = 0; i < 4; i++) {
                canvas[i] = document.getElementById("canvas"+i);
                ctx[i] = canvas[i].getContext("2d");
                ctx[i].fillStyle = "black";
                ctx[i].strokeStyle = colors[i];
                ctx[i].lineWidth = 2;
            }
            freq[0] = 1;
            freq[1] = 2;
            freq[2] = 3;
            phase[0] = 0;
            phase[1] = 0;
            phase[2] = 0;
            labelWaves();
            setInterval(animate, 40);
        }

        function labelWaves() {
            for (i = 0; i < 3; i++) {
                var phaseDeg = parseInt(phase[i] / Math.PI * 180);
                var labelString = 'Frequency: ' + freq[i] + ' &nbsp; Phase: ' + phaseDeg + '&deg;';
                label[i].innerHTML = labelString;
            }
        }

        function animate() {
            globalPhase = globalPhase + sixDeg;
            drawSinWave(0);
            drawSinWave(1);
            drawSinWave(2);
            drawAllWaves();
        }

        function drawSinWave (index) {
            var thisCtx = ctx[index];
            // clear to black
            thisCtx.fillRect(0, 0, canvasWidth, cHeight);
            // draw X axis
             var xAxis = cHeight / 2;
             thisCtx.beginPath();
             thisCtx.moveTo(canvasWidth,xAxis);
             thisCtx.lineTo(0, xAxis);
            // plot graph of sine wave
             var xCoord = 0;
             var steps = canvasWidth / freq[index];
             for (i = 0; i < freq[index]; i++) {
                 for (j = 0; j <= steps; j++) {
                     var xCoord = i * steps + j;
                     var radians = (aCircle / steps) * j + phase[index] + (globalPhase * freq[index]);
                     var sinY = Math.sin(radians);
                     var yCoord = sinY * vScale + xAxis;
                     thisCtx.lineTo(xCoord, yCoord);
                 }
             }
             thisCtx.stroke();
        }

        function drawAllWaves() {
            var thisCtx = ctx[3];
            thisCtx.fillRect(0, 0, canvasWidth, canvasHeight);
            // draw X axis
            thisCtx.beginPath();
            var xAxis = canvasHeight / 2;
            thisCtx.moveTo(canvasWidth, xAxis);
            thisCtx.lineTo(0, xAxis);
            // plot graph of all waves added together
            var xCoord = 0;
            for (i = 0; i < canvasWidth; i++) {
                var xCoord = i;
                var yCoord = 0;
                for (j = 0;j < 3; j++) {
                    var steps = canvasWidth / freq[j];
                    var radians = (aCircle / steps) * i + phase[j] + (globalPhase * freq[j]);
                    var sinY = Math.sin(radians);
                    yCoord += sinY;
                }
                yCoord = yCoord * vScale + xAxis;
                thisCtx.lineTo(xCoord, yCoord);
             }
            thisCtx.stroke();
        }

        function increment(index) {
            freq[index]++;
            drawSinWave(index);
            labelWaves();
        }

        function decrement(index) {
            freq[index]--;
            if (freq[index] < 0)
                freq[index] = 0;
            drawSinWave(index);
            labelWaves();
        }

        function addPhase(index) {
            var thePhase = phase[index] + ninetyDeg;
            if (parseInt(thePhase) == 6)
                thePhase = 0;
            phase[index] = thePhase;
            labelWaves();
            drawSinWave(index);
        }
    </script>
</head>
<body onload="init()">
    <p>
        <em>The canvas element is well-suited to display scientific or numeric data, especially interactive data.</em>
        <h1>Frequency Addition</h1>
        <div id="main" style="border: 5px inset #80e080; width:480px;">
            <div id="waves" style="margin: 5px; width: 200;">
                <b>Wave 1</b><br />
                <canvas id="canvas0" width="180" height="50">
                </canvas>
                <br />
                <b>Wave 2</b><br />
                <canvas id="canvas1" width="180" height="50">
                </canvas>
                <br />
                <b>Wave 3</b><br />
                <canvas id="canvas2" width="180" height="50">
                </canvas>
                <div>
                <br /><b>Addition of Waves 1, 2, and 3</b><br />
                <canvas id="canvas3" width="180" height="150">
                </canvas>
            </div>
        </div>
        <div id="controls" style="width: 120; margin: 5px; position:absolute; left:200px; top:118px;">

            <p id="label0">Freq: 1 Phase: 0</p>
            <input type="button" value=" ^ " onclick="increment(0)">
            <input type="button" value=" v " onclick="decrement(0)">
            <input type="button" value="+90&deg;" onclick="addPhase(0)">

            <p id="label1">Freq: 2 Phase: 0</p>
            <input type="button" value=" ^ " onclick="increment(1)">
            <input type="button" value=" v " onclick="decrement(1)">
            <input type="button" value="+90&deg;" onclick="addPhase(1)">

            <p id="label2">Freq: 3 Phase: 0</p>
            <input type="button" value=" ^ " onclick="increment(2)">
            <input type="button" value=" v " onclick="decrement(2)">
            <input type="button" value="+90&deg;" onclick="addPhase(2)">

        </div>
    </div>
    <p>Complex waveforms can be made by adding simple sine waves.</p>
    <p>Increase or decrease the frequencies and increment the phase of the component sine waves to see how they add together.</p>
</body>
</html>
```

[Next](Animating%20the%20Canvas.md)[Previous](Advanced%20Compositing.md)

