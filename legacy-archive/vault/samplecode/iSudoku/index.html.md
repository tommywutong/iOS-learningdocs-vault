---
title: iSudoku
apple_id: DTS10004395
resource_type: Sample Code
platform: Safari|iOS
topic: General
technology: null
published: '2007-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/iSudoku/Listings/index_html.html
archived_at: '2026-07-18T03:29:45.609963Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iSudoku](iSudoku.md)


[Next](iSudoku.css.md)[Previous](game-coordinates.html.md)

# index.html

```
<!--

 File: index.html

 Abstract: Content layout for iSudoku sample

 Version: <1.0>

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
 Apple Inc. ("Apple") in consideration of your agreement to the
 following terms, and your use, installation, modification or
 redistribution of this Apple software constitutes acceptance of these
 terms.  If you do not agree with these terms, please do not use,
 install, modify or redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software. 
 Neither the name, trademarks, service marks or logos of Apple Inc. 
 may be used to endorse or promote products derived from the Apple
 Software without specific prior written permission from Apple.  Except
 as expressly stated in this notice, no other rights or licenses, express
 or implied, are granted by Apple herein, including but not limited to
 any patent rights that may be infringed by your derivative works or by
 other works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2007 Apple Inc. All Rights Reserved.

 -->

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>iSudoku</title>
    <link rel="stylesheet" href="iSudoku.css" type="text/css">
    <script src="iSudoku.js" type="text/javascript"></script>
</head>
<body id="board-body">
<div id="board-div">
<table>
<tr>
<td>
  <table>
  <tr>
  <td id="cell0:0" class="board"></td>
  <td id="cell0:1" class="board"></td>
  </tr>
  <tr>
  <td id="cell0:2" class="board"></td>
  <td id="cell0:3" class="board"></td>
  </tr>
  </table>
</td>
<td>
  <table>
  <tr>
  <td id="cell1:0" class="board"></td>
  <td id="cell1:1" class="board"></td>
  </tr>
  <tr>
  <td id="cell1:2" class="board"></td>
  <td id="cell1:3" class="board"></td>
  </tr>
  </table>
</td>
</tr>

<tr>
<td>
  <table>
  <tr>
  <td id="cell2:0" class="board"></td>
  <td id="cell2:1" class="board"></td>
  </tr>
  <tr>
  <td id="cell2:2" class="board"></td>
  <td id="cell2:3" class="board"></td>
  </tr>
  </table>
</td>
<td>
  <table>
  <tr>
  <td id="cell3:0" class="board"></td>
  <td id="cell3:1" class="board"></td>
  </tr>
  <tr>
  <td id="cell3:2" class="board"></td>
  <td id="cell3:3" class="board"></td>
  </tr>
  </table>
</td>
</tr>
</table>
</div>
<div id="button-bar">

         <!-- Click on this button to start a new game -->
    <div class="menu-button" onclick="setupPuzzle();">New Game</div>

        <!-- Restart the current game. Put the game's initial values on the board. -->
    <div class="menu-button" onclick="document.puzzle.setup();">Start Over</div>
</div>

       <!-- Launch a dialog form that allow users to select a number or clear a value on the board  -->
<iframe src="iSudokuChooser.html" id="chooser-iframe"></iframe>
</body>
</html>
```

[Next](iSudoku.css.md)[Previous](game-coordinates.html.md)

