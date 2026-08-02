---
title: Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit
apple_id: TP40016060
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2015-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/iOSMultichannelMixerTest/Listings/Resources_info_html.html
archived_at: '2026-07-18T03:29:36.939635Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit](Using%20an%20AUGraph%20with%20the%20Multi-Channel%20Mixer%20and%20Remote%20I-O%20Audio%20Unit.md)


[Next](PublicUtility-CAComponentDescription.h.md)[Previous](Classes-MyViewController.h.md)

# Resources/info.html

```
<meta name = "viewport" content = "width = device-width">

<h4 align="left"iOS Multichannel Mixer Test</h4>

<p>Demonstrates the use of the AUGraph and related APIs. All the relevant code is
in the file MultichannelMixerController.mm. Touching the "Play Audio" button simply calls
AUGraphStart starting the graph initialized by the class, while "Stop Audio" will call
AUGraphStop. Audio data from each file is provided to the appropriate bus via the
renderInput Render Procedure. Each of the two input busses may be enabled or disabled
and volume controls are provided for both inputs and the mixer output.<p>

<hr align="center">

<p>Audio Unit Processing Graph Services provide interfaces for representing a set of
audio units, connections between their inputs and outputs, and callbacks used to provide
inputs. It also enables the embedding of sub (or child) processing graphs within parent
graphs to allow for a logical organization of parts of an overall signal chain.</p>

<p>An audio processing graph object (of type AUGraph) is a complete description of an
audio signal processing network. Audio Unit Processing Graph Services may manage the
instantiated audio units if the AUGraphOpen function is called.</p>

<p>An audio processing graph object may be introspected to get complete information
about all of the audio units in the graph. The various node objects (each of type AUNode)
in the graph, each representing an audio unit or a sub graph, may be added or removed,
and the interactions between them modified.</p>


<p>A graph object’s state can be manipulated in both the rendering thread and in other
threads. Consequently, any activities that affect the state of the graph are guarded with
locks and a messaging model between any calling thread and the thread upon which the
graph object’s output unit is called (the render thread).</p>

<p>A graph object will have a single head node-an output unit. The output unit is used to
both start and stop the rendering operations of a graph, and is the dispatch point for
the safe manipulation of the state of the graph while it is running.</p>
<br>
<br>
```

[Next](PublicUtility-CAComponentDescription.h.md)[Previous](Classes-MyViewController.h.md)

