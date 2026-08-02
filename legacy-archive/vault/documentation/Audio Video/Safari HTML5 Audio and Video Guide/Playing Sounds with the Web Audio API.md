---
title: Safari HTML5 Audio and Video Guide
apple_id: TP40009523
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/PlayingandSynthesizingSounds/PlayingandSynthesizingSounds.html
archived_at: '2026-07-15T05:21:33.328529Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Audio and Video Guide](About%20HTML5%20Audio%20and%20Video.md)


[Next](Controlling%20Media%20with%20JavaScript.md)[Previous](iOS-Specific%20Considerations.md)

# Playing Sounds with the Web Audio API

In [Audio and Video HTML](Audio%20and%20Video%20HTML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqmrnknltc), you learned how to stream audio using the `<audio>` HTML5 element. While the `<audio>` tag is suitable for basic needs such as streaming and media playback, another option called the Web Audio API offers a more comprehensive audio-based toolkit. The Web Audio API is a JavaScript interface that features the ability to:

- Play a sound at a precise moment in time.
- Synthesize aural tones and oscillations.
- Mix sound effects with filters.
- Access the raw bits of audio data.

Some use cases of the Web Audio API include supplementing HTML5 games with sound effects, controlling DJ-style music players, and visualizing music in new, innovative ways. Harness the power of the Web Audio API to create new web experiences that are augmented with sound.

In this chapter you’ll learn how to start using the Web Audio API in your web apps.

Before you can play any sounds, you must first create an audio context from which the sound can play. Similar to how HTML5 canvas requires a context on which lines and curves are drawn, Web Audio requires an audio context on which sounds are played and manipulated. This context will be the parent object of further audio objects to come.

```
if('webkitAudioContext' in window) {
    var myAudioContext = new webkitAudioContext();
}
```

Your audio context is typically created when your page initializes and should be long-lived. You can play multiple sounds coming from multiple sources within the same context, so it is unnecessary to create more than one audio context per page.

Once an audio context has been instantiated, fetch your sounds from the disk or from a server. Load all the sounds upfront that you anticipate could play to avoid a delay caused by network transmission. Then, buffer the sounds so that they’re ready to be played at a moment’s notice. The buffer is essentially a nonpersistent cache that allows you to replay sounds repeatedly without needing to reload the resource.

You load sounds with an asynchronous `XMLHttpRequest`. Set the response type of the request to `arraybuffer`, which interprets the audio file as binary data. Add an event listener on the request to capture the sound buffer as soon as it loads.

```
request = new XMLHttpRequest();
request.open('GET', 'explosion.aiff', true);
request.responseType = 'arraybuffer';
request.addEventListener('load', bufferSound, false);
request.send();
```

When the resource loads, pass the response of the AJAX request to the `createBuffer()` function on your audio context. Below is the `bufferSound()` callback function that is referred to above in the event listener.

```
var mySource;
function bufferSound(event) {
    var request = event.target;
    var source = myAudioContext.createBufferSource();
    source.buffer = myAudioContext.createBuffer(request.response, false);
    mySource = source;
}
```

Instead of calling `createBuffer()` directly, you can create a buffer by using the `decodeAudioData()` function on your audio context. The `decodeAudioData()` function provides an optional third parameter you can use to catch errors.

If you want to pull the audio of an `<audio>` or `<video>` element that’s already on the page, you can bypass both the `XMLHttpRequest` creation and manual buffering steps by calling your audio context’s `createMediaElementSource()` function. Pass a reference to your desired media element to return a buffered source. This can be used, for example, to change the pitch of the video’s sound dynamically while the video plays.

Instead of loading a preexisting audio file, you can generate sounds with the Oscillator object. Oscillators are great for creating beeps and single notes. Create an oscillator with the `createOscillator()` constructor, and assign a waveform to its `type` property. Acceptable values for the `type` property are listed in [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnrnknlts).

__Table 3-1__  Types of periodic waveforms

| Type | Waveform |
| `0` | Sine wave |
| `1` | Square wave |
| `2` | Sawtooth wave |
| `3` | Triangle wave |

```
var source = myAudioContext.createOscillator();
source.type = 0; // sine wave
```

You can also assign a custom waveform to the oscillator by creating a wave table. In the following example, a waveform is created by using sine and cosine waves:

```
var curveLength = 100;
var curve1 = new Float32Array(curveLength);
var curve2 = new Float32Array(curveLength);
for (var i = 0; i < curveLength; i++)
    curve1[i] = Math.sin(Math.PI * i / curveLength);

for (var i = 0; i < curveLength; i++)
    curve2[i] = Math.cos(Math.PI * i / curveLength);

var waveTable = myAudioContext.createWaveTable(curve1, curve2);
source.setWaveTable(waveTable);
```

Oscillators produce tonal sounds. You can adjust the sound of the emitted tones in the same fashion as adjusting any source, as further described in, [Routing and Mixing Sounds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnrnknlto).

Now that you have your source buffered or synthesized, for sound to emit from your speakers you need to connect your source to a destination. You can route your source through a complex graph of nodes (which is covered in the next section, [Routing and Mixing Sounds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnrnknlto)), but for now, connect it directly to the destination of your audio context. You can do this by passing the `destination` property of your audio context to the `connect()` function of your source.

```
source.connect(myAudioContext.destination);
```

Connecting a source to a destination is like hooking up an electric guitar to an amplifier: the input needs to connect to the output in order to create an audible sound. The `destination` property always correlates to the default hardware output of sound, whether it’s through speakers, attached headphones, or a Bluetooth headset.

To play the sound immediately, call the `noteOn(0)` function on your source object.

```
// play right now (0 seconds from now)
source.noteOn(0);
```

To stop playing the sound immediately, call `noteOff(0)` on your source. Instead of `0`, you can also pass the `currentTime` property of your audio context.

By specifying a time, you can schedule a precise beat or rhythm for your sounds to start playing. If the beat is steady and consistent, you can choose to call `noteOn(0)` in a `setInterval()` with the interval of your choice. Otherwise, you can calculate when the sounds will play in the future, and call `noteOn()` in a loop with the relative playtimes as the argument.

```
// play 8 notes evenly spaced over the course of a half-second
for (var i = 0; i < 8; i++) {
    var rest = i / 16;
    source.noteOn(myAudioContext.currentTime + rest);
}
```


The beauty behind the Web Audio API is that you can insert a graph of audio nodes between your source and destination to alter the voice of the sound. This concept mimics a guitarist’s pedal board. Electric guitarists pass their raw audio input through pedals, or audio filter effects, before the sound plays as audible output. This gives them finer control to transmogrify their audio output. Just like how a musician can string together a chain of pedals, you can create an intricate network of multiple audio sources and filters to modify your produced sound.

The example below routes the input source through a compressor, then a reverberation modifier, and then a volume control, before the sound is played.

```
var compressor = myAudioContext.createDynamicsCompressor();
var reverb = myAudioContext.createConvolver();
var volume = myAudioContext.createGainNode();

// connect source through a series of filters
source.connect(compressor);
compressor.connect(reverb);
reverb.connect(volume);
volume.connect(myAudioContext.destination);

source.noteOn(0);
```

Imagine a guitar that’s hooked up to a chain of pedals, which then feeds into an amp. The `connect()` function is metaphorically a cable connecting audio equipment together.

There are many filter effects from which to choose; one of the most commonly used and most helpful to include in your virtual pedal board is a compressor. Compressors boost soft tones and diminish loud tones, normalizing the audio output so that there are no parts that are extremely quiet or extremely loud. This creates a more pleasant listening experience and prevents strain on the listener’s ears. While this effect is beneficial in the majority of cases, there are some instances when a compressor would not be desired—for example, someone listening to classical music would want to hear every subtle pianissimo and grand fortissimo.

You can also mix several sources together to play out of the same destination. This is useful for crossfading between two tracks: with one set of controls, you can manage two separate sources simultaneously. Just instantiate a new source as described in [Fetching and Buffering Sounds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnrnknltg) or [Synthesizing Sounds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnrnknlti), and connect it to the same destination.

Access the raw data of the audio output by routing your sound through a real-time analyser node. Use your imagination and creativity to come up with interfaces for playing and visualizing sound.

[Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnrnknltcna) selects a sound at random, passes the sound through audio filters, and loops the sound while the audio spectrum is drawn on an HTML5 canvas, as shown in [Figure 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnrnknltcni). It also provides controls for adjusting filter properties and pausing a playing sound.

__Figure 3-1__  A simple synthesizer and audio spectrum visualizer

!

__Listing 3-1__  A simple synthesizer and audio spectrum visualizer

```
<!doctype html>
<html>
<head>
    <title>mySynth</title>
    <script>
        const PATH = '/System/Library/Sounds/',
              SOUNDS = ['Basso', 'Blow', 'Bottle', 'Frog', 'Funk', 'Glass', 'Hero',
                        'Morse', 'Ping', 'Pop', 'Purr', 'Sosumi', 'Submarine', 'Tink'];
        var myAudioContext, myAudioAnalyser,
            myBuffers = {}, mySource,
            myNodes = {},   mySpectrum,
            isPlaying = false;

        function init() {
            if('webkitAudioContext' in window) {
                myAudioContext = new webkitAudioContext();
                // an analyser is used for the spectrum
                myAudioAnalyser = myAudioContext.createAnalyser();
                myAudioAnalyser.smoothingTimeConstant = 0.85;
                myAudioAnalyser.connect(myAudioContext.destination);

                fetchSounds();
            }
        }

        function fetchSounds() {
            var request = new XMLHttpRequest();
            for (var i = 0, len = SOUNDS.length; i < len; i++) {
                request = new XMLHttpRequest();
                // the underscore prefix is a common naming convention
                // to remind us that the variable is developer-supplied
                request._soundName = SOUNDS[i];
                request.open('GET', PATH + request._soundName + '.aiff', true);
                request.responseType = 'arraybuffer';
                request.addEventListener('load', bufferSound, false);
                request.send();
            }
        }

        function bufferSound(event) {
            var request = event.target;
            var buffer = myAudioContext.createBuffer(request.response, false);
            myBuffers[request._soundName] = buffer;
        }

        function selectRandomBuffer() {
            var rand = Math.floor(Math.random() * SOUNDS.length);
            var soundName = SOUNDS[rand];
            return myBuffers[soundName];
        }

        function routeSound(source) {
            myNodes.filter = myAudioContext.createBiquadFilter();
            myNodes.panner = myAudioContext.createPanner();
            myNodes.volume = myAudioContext.createGainNode();
            // var compressor = myAudioContext.createDynamicsCompressor();

            // set node values to current slider values
            var highpass = document.querySelector('#highpass').value;
            var panX = document.querySelector('#pan').value;
            var volume = document.querySelector('#volume').value;

            myNodes.filter.type = 1; // highpass
            myNodes.filter.frequency.value = highpass;
            myNodes.panner.setPosition(panX, 0, 0);
            myNodes.volume.gain.value = volume;

            // pass source through series of nodes
            source.connect(myNodes.filter);
            myNodes.filter.connect(myNodes.panner);
            myNodes.panner.connect(myNodes.volume);
            myNodes.volume.connect(myAudioAnalyser);

            return source;
        }

        function playSound() {
            // create a new AudioBufferSourceNode
            var source = myAudioContext.createBufferSource();
            source.buffer = selectRandomBuffer();
            source.loop = true;
            source = routeSound(source);
            // play right now (0 seconds from now)
            // can also pass myAudioContext.currentTime
            source.noteOn(0);
            mySpectrum = setInterval(drawSpectrum, 30);
            mySource = source;
        }

        function pauseSound() {
            var source = mySource;
            source.noteOff(0);
            clearInterval(mySpectrum);
        }

        function toggleSound(button) {
            if(!isPlaying) {
                playSound();
                button.value = "Pause sound";
                isPlaying = true;
            }
            else {
                pauseSound();
                button.value = "Play random sound";
                isPlaying = false;
            }
        }

        function drawSpectrum() {
            var canvas = document.querySelector('canvas');
            var ctx = canvas.getContext('2d');
            var width = canvas.width;
            var height = canvas.height;
            var bar_width = 10;

            ctx.clearRect(0, 0, width, height);

            var freqByteData = new Uint8Array(myAudioAnalyser.frequencyBinCount);
            myAudioAnalyser.getByteFrequencyData(freqByteData);

            var barCount = Math.round(width / bar_width);
            for (var i = 0; i < barCount; i++) {
                var magnitude = freqByteData[i];
                // some values need adjusting to fit on the canvas
                ctx.fillRect(bar_width * i, height, bar_width - 2, -magnitude + 60);
            }
        }

        function sliderChange(slider) {
            if(myAudioContext.activeSourceCount > 0) {
                if(slider.id == 'highpass') {
                    var highpass = slider.value;
                    myNodes.filter.frequency.value = highpass;
                }
                else if(slider.id == 'pan') {
                    var panX = slider.value;
                    myNodes.panner.setPosition(panX, 0, 0);
                }
                else if(slider.id == 'volume') {
                    var volume = slider.value;
                    myNodes.volume.gain.value = volume;
                }
            }
        }
    </script>
    <style>
        input { display: block; }
    </style>
</head>
<body onload="init()">
    <input id="play" onclick="toggleSound(this)" type="button" value="Play random sound" />

    <span>Highpass:</span>
    <input id="highpass" onchange="sliderChange(this)" type="range" min="0" max="1024" step="1" value="512" />
    <span>Pan:</span>
    <input id="pan" onchange="sliderChange(this)" type="range" min="-3" max="3" step="0.01" value="0" />
    <span>Volume:</span>
    <input id="volume" onchange="sliderChange(this)" type="range" min="0" max="1" step="0.01" value="1" />

    <canvas width="300" height="200"></canvas>
</body>
</html>
```

[Next](Controlling%20Media%20with%20JavaScript.md)[Previous](iOS-Specific%20Considerations.md)

