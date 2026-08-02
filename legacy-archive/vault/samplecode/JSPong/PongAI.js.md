---
title: JSPong
apple_id: DTS10004362
resource_type: Sample Code
platform: macOS
topic: Languages & Utilities
technology: JavaScriptCore
published: '2007-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/JSPong/Listings/PongAI_js.html
archived_at: '2026-07-18T03:13:12.614585Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JSPong](JSPong.md)


[Next](PongAI.m.md)[Previous](PongAI.h.md)

# PongAI.js

```
var lastBallY = 0;

function nextMove(paddle, ball)
{
    var ballY = ball.middleY;
    var ballDirection = ballY > lastBallY
        ? kUpDirection 
        : kDownDirection;
    lastBallY = ballY;

    if (ballY > paddle.top)
        return kUpDirection;

    if (ballY < paddle.bottom)
        return kDownDirection;

    return ballDirection;
}
```

[Next](PongAI.m.md)[Previous](PongAI.h.md)

