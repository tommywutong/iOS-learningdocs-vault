---
title: 'MPSCNNHelloWorld: Simple Digit Detection Convolution Neural Networks (CNN)'
apple_id: TP40017482
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal Performance Shaders
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/MPSCNNHelloWorld/Listings/MPSCNNHelloWorld_atomics_h.html
archived_at: '2026-07-18T03:13:59.843381Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPSCNNHelloWorld: Simple Digit Detection Convolution Neural Networks (CNN)](MPSCNNHelloWorld-%20Simple%20Digit%20Detection%20Convolution%20Neural%20Networks%20%28CNN%29.md)


[Next](MPSCNNHelloWorld-SlimMPSCNN.swift.md)[Previous](MPSCNNHelloWorld-ViewController.swift.md)

# MPSCNNHelloWorld/atomics.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    We define some custom atomics to be used the network so seperate threads at end of commandBuffers can safely increment.
*/

#ifndef atomics_h
#define atomics_h

#import <stdatomic.h>

static atomic_int cnt = ATOMIC_VAR_INIT(0);
void __atomic_increment();
void __atomic_reset();
int __get_atomic_count();

#endif /* atomics_h */
```

[Next](MPSCNNHelloWorld-SlimMPSCNN.swift.md)[Previous](MPSCNNHelloWorld-ViewController.swift.md)

