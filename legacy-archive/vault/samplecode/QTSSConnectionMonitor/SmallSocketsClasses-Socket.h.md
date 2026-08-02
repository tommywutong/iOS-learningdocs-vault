---
title: QTSSConnectionMonitor
apple_id: DTS10001049
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSConnectionMonitor/Listings/SmallSocketsClasses_Socket_h.html
archived_at: '2026-07-18T03:21:18.982575Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSConnectionMonitor](QTSSConnectionMonitor.md)


[Next](SmallSocketsClasses-Socket.m.md)[Previous](SmallSocketsClasses-AbstractSocket.m.md)

# SmallSocketsClasses/Socket.h

```objc
//
// Socket.h
//
// SmallSockets Library (http://smallsockets.sourceforge.net/)
//
// Copyright (C) 2001 Steven Frank (stevenf@panic.com)
//
// This software is provided 'as-is', without any express or implied 
// warranty. In no event will the authors be held liable for any damages 
// arising from the use of this software.
//
// Permission is granted to anyone to use this software for any purpose, 
// including commercial applications, and to alter it and redistribute it 
// freely, subject to the following restrictions:
//
//     1. The origin of this software must not be misrepresented; you must 
//        not claim that you wrote the original software. If you use this 
//        software in a product, an acknowledgment in the product 
//        documentation (and/or about box) would be appreciated but is not 
//        required.
//
//     2. Altered source versions must be plainly marked as such, and must
//        not be misrepresented as being the original software.
//
//     3. This notice may not be removed or altered from any source 
//        distribution.
//        

#import "AbstractSocket.h"

@interface Socket : AbstractSocket 
{
}

// Convenience constructor

+ (Socket*)socket;

// Receiving connections

- (Socket*)acceptConnectionAndKeepListening;

@end
```

[Next](SmallSocketsClasses-Socket.m.md)[Previous](SmallSocketsClasses-AbstractSocket.m.md)

