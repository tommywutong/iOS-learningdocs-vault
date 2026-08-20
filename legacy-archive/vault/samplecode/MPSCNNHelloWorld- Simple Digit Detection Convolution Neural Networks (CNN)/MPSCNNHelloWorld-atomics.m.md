---
title: 'MPSCNNHelloWorld: Simple Digit Detection Convolution Neural Networks (CNN)'
apple_id: TP40017482
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal Performance Shaders
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/MPSCNNHelloWorld/Listings/MPSCNNHelloWorld_atomics_m.html
archived_at: '2026-07-18T03:13:59.878154Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MPSCNNHelloWorld: Simple Digit Detection Convolution Neural Networks (CNN)](MPSCNNHelloWorld-%20Simple%20Digit%20Detection%20Convolution%20Neural%20Networks%20%28CNN%29.md)


[Next](MPSCNNHelloWorld-ViewController.swift.md)[Previous](MPSCNNHelloWorld-%20Simple%20Digit%20Detection%20Convolution%20Neural%20Networks%20%28CNN%29.md)

# MPSCNNHelloWorld/atomics.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    We define some custom atomics to be used the network so seperate threads at end of commandBuffers can safely increment.
*/

#import "atomics.h"

void __atomic_increment(){
    atomic_fetch_add(&cnt, 1);
}
void __atomic_reset(){
    cnt = ATOMIC_VAR_INIT(0);
}
int __get_atomic_count(){
    return atomic_load(&cnt);
}
```

[Next](MPSCNNHelloWorld-ViewController.swift.md)[Previous](MPSCNNHelloWorld-%20Simple%20Digit%20Detection%20Convolution%20Neural%20Networks%20%28CNN%29.md)

