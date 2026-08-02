---
title: iSudoku
apple_id: DTS10004395
resource_type: Sample Code
platform: Safari|iOS
topic: General
technology: null
published: '2007-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/iSudoku/Listings/iSudoku_css.html
archived_at: '2026-07-18T03:29:45.453013Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iSudoku](iSudoku.md)


[Next](iSudoku.js.md)[Previous](index.html.md)

# iSudoku.css

```
/*

 File: iSudoku.css 

 Abstract: CSS properties for the iSudoku sample

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
*/


* {
    font-family: 'Lucida Grande', Verdana, sans-serif;


}

#board-body {
    margin: 5px 8px 5px 9px;
    -webkit-text-size-adjust: none;
}

#chooser-body {
    margin: 0px;
    padding: 0px;
    -webkit-text-size-adjust: none;
}

#board-div {
    width: 300px;
}

#button-bar {
    background-image: url(button-bar.png);
    background-repeat: repeat-x;
    text-align: center;
    width: 300px;
    height: 43px;
}

#chooser-button-blocker {
    position: absolute;
    top: 311px;
    left: 0px;
    height: 38px;
    width: 300px;
}

#chooser-background {
    position: absolute;
    top: 0px;
    left: 4px;
    background-color: black;
    opacity: 0.75;
    height: 302px;
    width: 300px;
}

#chooser-grid-div {
    position: absolute;
    top: 74px;
    left: 21px;
    width: 254px;
    opacity: 1.0;
    background-color: #000f37;
    border: 2px solid white;
    -webkit-border-radius: 10px;
    padding: 5px;
}

#chooser-grid {
    border: 0px none black;
    padding: 0px;
    margin: 0px auto;
    text-align: center;
}

#chooser-grid > tr > td {
    padding: 2px;
}

#chooser-iframe {
    border: 0px none black;
    top: 5px;
    left: 5px;
    height: 350px;
    width: 310px;
    display: none;
    z-index: -1;
}

table {
    border-spacing: 0px;
}

td {
    padding: 0px;
    border: 1px solid black;
}

td.board {
    border: 1px solid black;
    height: 73px;
    width: 73px;
    text-align: center;
    vertical-align: middle;
    font-size: 32px;
}

td.chooser {
    border: 0px none black;
}

td.chooserLeft {
    border: 0px none black;
    width:20%;
}
td.chooserMiddle{
    border: 0px none black;
    width:60%;
}
#chooser-title {
    color: white;
    text-align: center;
    font-weight: bold;
    margin: 5px;
}

#chooser-message {
    color: white;
    text-align: center;
    font-weight: regular;
    padding: 5px;
}

div.default-alert-button {
    color: white;
    font-weight: bold;
    text-align: center;
    padding: 10px 0px;
    width: 125px;
    border: 1px solid black;
    -webkit-border-radius: 5px;
    background-color: #576285;
    opacity: 1.0;
}

div.alert-button {
    color: white;
    font-weight: bold;
    text-align: center;
    padding: 10px 0px;
    width: 125px;
    border: 1px solid black;
    -webkit-border-radius: 5px;
    background-color: #37456c;
    opacity: 1.0;
}

div.menu-button {
    display: inline-block;
    color: white;
    font-weight: bold;
    font-size: 12px;
    text-align: center;
    padding: 7px 0px;
    width: 80px;
    border: 1px solid black;
    -webkit-border-radius: 5px;
    background-color: #486a9a;
    opacity: 1.0;
    margin: 6px;
}
```

[Next](iSudoku.js.md)[Previous](index.html.md)

