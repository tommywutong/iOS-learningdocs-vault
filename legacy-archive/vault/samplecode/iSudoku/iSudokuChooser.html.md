---
title: iSudoku
apple_id: DTS10004395
resource_type: Sample Code
platform: Safari|iOS
topic: General
technology: null
published: '2007-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/iSudoku/Listings/iSudokuChooser_html.html
archived_at: '2026-07-18T03:29:45.316918Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iSudoku](iSudoku.md)


[Next](iSudokuChooser.js.md)[Previous](iSudoku.js.md)

# iSudokuChooser.html

```
<!--

 File: iSudokuChooser.html 

 Abstract: Content layout that provides iSudoku player
           with numbers ranging from 1 to 4 for the board.

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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>iSudoku Chooser</title>
    <link rel="stylesheet" href="iSudoku.css" type="text/css">
    <script src="iSudokuChooser.js" type="text/javascript"></script>
</head>
<body id="chooser-body">
    <div id="chooser-background"></div>
    <div id="chooser-grid-div">
    <div id="chooser-title">Select a Number</div>
    <table id="chooser-grid">
        <tr>
            <td class="chooser"><div class="alert-button" onclick="setValue('1');">1</div></td>
            <td class="chooser"><div class="alert-button" onclick="setValue('2');">2</div></td>
        </tr>
        <tr>
            <td class="chooser"><div class="alert-button" onclick="setValue('3');">3</div></td>
            <td class="chooser"><div class="alert-button" onclick="setValue('4');">4</div></td>
        </tr>
        <tr>
            <td class="chooser"><div class="alert-button" onclick="setValue(' ');">Clear</div></td>
            <td class="chooser"><div class="default-alert-button" onclick="dismiss();">Cancel</div></td>
        </tr>
    </table>
    </div>
    <div id="chooser-button-blocker"></div>
    <p><input type="hidden" name="id"></p>
</body>
</html>
```

[Next](iSudokuChooser.js.md)[Previous](iSudoku.js.md)

