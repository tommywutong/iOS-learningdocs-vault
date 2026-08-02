---
title: How Do I Leverage Data in a Trained Network For Use With MPS CNN?
apple_id: DTS40017619
resource_type: QA
platform: tvOS|iOS
topic: Mathematical Computation
technology: Metal Performance Shaders
published: '2017-03-21'
source_url: https://developer.apple.com/library/archive/qa/qa1953/_index.html
archived_at: '2026-07-18T02:37:53.691455Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1953

# How Do I Leverage Data in a Trained Network For Use With MPS CNN?

## Q:  How Do I Leverage Data in a Trained Network For Use With MPS CNN?

A: In iOS 10 and tvOS 10, the Metal Performance Shaders (MPS) framework introduced Convolutional Neural Networks (CNN) for deep learning using previously obtained training data.

This Q&A describes how to leverage data in a trained network so that a query can be run against it, and is demonstrated in the following sample project:

[MPSCNNHelloWorld](https://developer.apple.com/library/content/samplecode/MPSCNNHelloWorld/Introduction/Intro.html)

which shows how to encode different layers to the GPU and perform image recognition using trained parameters (weights and bias) that have been fetched from the pre-trained, and saved, network on TensorFlow (see networks trained on [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)).

This Python script is used to convert tensorFlow tensors to MPS format .dat files for the sample:

__Listing 1__  tensorFlow data import script

```
import tensor flow as tf
import bumpy as np
sess = tf.InteractiveSession()

def weight_variable(shape):
   initial = tf.truncated_normal(shape, stddev=0.1)
   return tf.Variable(initial)
W_conv1 = weight_variable([5, 5, 1, 32])

a = sess.run(W_conv1)
# changing from tensorFlow order of weights [kH kW iC oC] to MPS accepted order of weights i.e. [oC kH kW iC]
a = np.swapaxes(a,2,3)
a = np.swapaxes(a,1,2)
a = np.swapaxes(a,0,1)

a.astype(‘float32’).tofile(‘weights_conv1.dat’)
```

Once the .dat files are created, the sample's main view controller is able to load and memory map the data using the CNN helper classes SlimMPSCNNConvolution and SlimMPSCNNFullyConnected.

This Swift code, which is similar to but not present in the sample, details the mapping of weights, which are declared the same way as biases:

__Listing 2__  MPS CNN instantiation with weights

```
var numberOfOutputChannels = 2 //oC is the index into it
var numberOfInputChannels = 1  //iC is the index into it
var kernelWidth = 2            //kW is the index into it
var kernelHeight = 2           //kH is the index into it

var weights = [1.0,  2.0,  3.0,  4.0, 5.0,  6.0,  7.0,  8.0]
//             iC=0  iC=0  iC=0  iC=0 iC=0  iC=0  iC=0  iC=0
//             kW=0  kW=1  kW=0  kW=1 kW=0  kW=1  kW=0  kW=1
//             kH=0  kH=0  kH=1  kH=1 kH=0  kH=0  kH=1  kH=1
//             oC=0  oC=0  oC=0  oC=0 oC=1  oC=1  oC=1  oC=1

MPSCNNConvolution.init(device: device,
          	      convolutionDescriptor: convDesc,
                      kernelWeights: weights,
                      biasTerms: b,                       // declared same way as weights
                      flags: MPSCNNConvolutionFlags.none)
```

You can pass in the weights array as the argument for `kernelWeights` as is because it is accepted as a valid unsafePointer for this argument.

Generally speaking, the MPSCNNConvolution class takes weights in the order weight[outputChannels][kernelHeight][kernelWidth][inputChannels/groups] and this information is in the header file MPSCNN.h.

In the sample project, MNIST_Full_LayerNN uses SlimMPSCNNFullyConnected to instantiate the MPSCNNConvolution kernel (see [MPSCNNConvolution's init](https://developer.apple.com/reference/metalperformanceshaders/mpscnnconvolution/1648861-init)).

Now we're ready to run a query. Assuming we've selected a single layer network, we draw a digit in the App's UI and attempt to recognize it via a forward pass through the network using an instance of MNIST_Full_LayerNN. The operation for a deep network is similar.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-03-21 | New document that describes the data formats and resources for configuring Metal CNN |

