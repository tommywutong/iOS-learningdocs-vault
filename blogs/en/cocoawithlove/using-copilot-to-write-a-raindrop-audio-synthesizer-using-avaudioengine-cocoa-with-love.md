---
title: 'Using Copilot to write a raindrop audio synthesizer using AVAudioEngine | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/copilot-raindrop-generator.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:b719e688e4253325'
translated: false
---

> 原文：[Using Copilot to write a raindrop audio synthesizer using AVAudioEngine | Cocoa with Love](https://www.cocoawithlove.com/blog/copilot-raindrop-generator.html)　·　Cocoa with Love (Matt Gallagher)

I’ve largely ignored the use of large language models (LLMs) as programming assistants, despite (or because of) the hype of the last 2 years. I’ve had a preconception that an LLM might not work well enough or might not meet my expectations of code quality.

Since Microsoft have recently made the lowest tier of [GitHub Copilot for VS Code free](https://code.visualstudio.com/blogs/2024/12/18/free-github-copilot), I wanted to test that preconception and see how helpful LLM-assisted programming might be when implementing a small project in Swift. And maybe this will make an interesting point of comparison to [Apple’s Swift Assist](https://www.apple.com/newsroom/2024/06/apple-empowers-developers-and-fuels-innovation-with-new-tools-and-resources/) (if and when that’s finally available).

As for the project itself: I wanted to explore sound synthesis using `AVAudioEngine` after stumbling across [a GitHub repository that implied a raindrop could be synthesized using a very simple waveform](https://github.com/747745124/Raindrop-Generator). It seems unlikely that a simple waveform would produce a convincing raindrop sound but the project should be well within the “few thousand line” context limit for an LLM so I think it’s an achievable goal.

> **On calling everything “AI”**: LLMs are commonly referred to as “AI” but the description makes me uncomfortable. I wrote my engineering thesis using neural networks more than 20 years ago and we never used the term “AI”. The terms used were always “neural networks” or “machine learning”. “AI” has always implied a more-general intelligence and I associate it with people deceptively implying that tools are smarter than they are or that general intelligence is just around the corner.

## The setup

I’m running Visual Studio Code 1.96.2 and using its built-in connection to Github Copilot (GPT 4o) that is currently free to use if you authorise via your GitHub account. In VS Code, I’ve installed the Swift v1.11.4 extension for Swift language server support and SweetPad 0.1.48 for building via Xcode and ensuring VS Code behaves better on Xcode Projects.

If you haven’t used SweetPad before, you need to set it up for each project by typing _Command-Shift-P_ in VS Code and choosing “SweetPad: Generate Build Server Config” from the popup that appears and then selecting the build target so it can create a buildServer.json file. Additionally, the Swift extension might ask to configure itself (global is usually fine).

If you aren’t prompted when you launch VS Code, you may need to [enable Copilot Free in VS Code to configure Copilot](https://code.visualstudio.com/docs/copilot/setup-simplified). When you want to ask Copilot something, press _Command-Control-I_ and that will present a chat window where you can prompt Copilot to write new code or refactor existing code.

I haven’t really spent enough time configuring VS Code the way I like it so outside of interacting with Copilot, I’m likely to do most of my editing, building and running in Xcode itself.

> **Check it out**: you can [download the code for this article from the RainGenerator repository](https://github.com/mattgallagher/RainGenerator). The commit history includes most of the steps discussed in this article.

### Alternative setup

Not to offer too much of a peek behind the curtain but I ran this same experiment nearly a month ago using [Cursor](https://www.cursor.com) (a fork of Visual Studio Code designed to focus on these LLM-based workflows). Thomas Ricouard has written [a pretty good article on using Cursor for iOS development](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941), if you’d like to know more. I think the Claude 3.5 LLM that Cursor uses by default did produce slightly better code than Copilot but the difference between VS Code and Cursor or Copilot and Claude wasn’t huge (the broad strokes are identical between each). This article will focus on my Copilot experience since I didn’t really document my Cursor experience (although the first commit in the repository still has a date of December 1 from the Cursor timeline).

## Tone Generator

### First effort

I wanted to start the project simple so to begin, I thought I’d ask Copilot to do something very simple [that I’ve written about before: a tone generator](https://www.cocoawithlove.com/2010/10/ios-tone-generator-introduction-to.html). That code involves a huge amount of boilerplate that shouldn’t be rerequired in `AVAudioEngine` (the latest iteration of the same audio processing graph concept).

While I’ve read about `AVAudioEngine` (introduced between macOS 10.10 and 10.15) I haven’t really had the chance to use it so maybe Copilot can show me how it’s done.

> **Prompt:** Create a Tone Generator that plays a sine, square, or sawtooth waveform and offers sliders to control volume and frequency.

The only context I’ve provided to Copilot is a `ContentView.swift` file, so I’m hoping it will understand that I’d like a SwiftUI interface. But I haven’t mentioned `AVAudioEngine`.

How does Copilot fair?

![Copilot’s first effort](https://www.cocoawithlove.com/assets/blog/copilot-tone-generator-1.png)

<sub>Copilot’s first effort</sub>

It has created an `AudioEngine` class that tries to render to a PCM buffer and play that in a loop. But it looks clunky (there’s no real need for separate “Play” and “Stop” buttons and that “Frequency” slider is using a step size of 1 with 2000 steps, making it slow and largely unusable) but worst of all, **it doesn’t work**. Hitting play throws an exception.

Not a great start.

Looking at the code, it’s pretty simple to see that the exception is because the `format` in the `init` function – as used to connect the player to the `outputNode` – is not the same as the `format` used in the `start` function and the mismatch is leading to a runtime exception.

```swift
    init() {
        engine.attach(player)
        let format = engine.outputNode.inputFormat(forBus: 0)
        engine.connect(player, to: engine.outputNode, format: format)
        try? engine.start()
    }

    func start(waveform: Waveform, frequency: Double, volume: Double) {
        let sampleRate = 44100
        let length = AVAudioFrameCount(sampleRate)
        let format = AVAudioFormat(standardFormatWithSampleRate: Double(sampleRate), channels: 1)!
        buffer = AVAudioPCMBuffer(pcmFormat: format, frameCapacity: length)
        buffer?.frameLength = length
```

Let’s see if Copilot can sort out this problem.

> **Prompt:** The AudioEngine isn’t making a sound. Can you identify what is wrong?

Copilot adds a catch around the creation of the `AVAudioEngine` (previously it was using a `try?`):

```swift
do {
    try engine.start()
} catch {
    print("Error starting audio engine: \(error.localizedDescription)")
}
```

Yeah, it didn’t have a clue.

Maybe if I give Copilot the exact exception, it can fix the problem.

> **Prompt:** Can you fix the following exception that is thrown when scheduleBuffer is called: “required condition is false: [AVAudioPlayerNode.mm:740:ScheduleBuffer: (_outputFormat.channelCount == buffer.format.channelCount)]”

With this, Copilot does make the audio play – by changing the `format` line in the `start` function to:

```swift
let format = engine.outputNode.inputFormat(forBus: 0)
```

However, even though the audio plays, it is mono, in the left speaker only. A proper fix would have been to take the `format`, as defined in the `start` function, and use it when connecting the `player` in the `init` function. I can do that manually and if I also remove the `step` from the Frequency slider in the UI (so the app doesn’t hang when trying to draw the slider), then the app “works”.

### Second effort

I want to see if Copilot can handle a bit of cleanup if I give it the steps. Instead of pre-rendering a PCM buffer and looping that, I prefer to use a render function that generates the audio-on-the-fly.

> **Prompt:** Refactor the AudioEngine to generate audio using an AVAudioSourceNode render block that calls a generateSample function. Move the @State variables from the ContentView into the AudioEngine and make the ContentView observe the AudioEngine.

Copilot follows all my instructions and the code now ends up _looking_ better but it has gone from “working” to “not working”, again. Now the tone plays immediately on application startup and the “Play” and “Stop” buttons no longer work.

For some reason, alongside the requested changes, Copilot decided to change the `start` and `stop` functions to set the `engine.mainMixerNode.outputVolume` to 1 or 0 (instead of actually pausing the audio generation). This is a bad idea (you should either pause or stop when audio generation is paused by the user). But it doesn’t work because in the current state, the `mainMixerNode` is not being added to the graph at all, so setting volume on it has no effect.

Getting a little exhausted with these issues, I resort to manually editing the code: calling `start()` and `stop()` on the engine instead of changing the volume, removing the `step` parameter from the frequency slider that was making it practically unusable and replacing the separate “Play” and “Stop” buttons with a single toggle button that changes its label.

So far, I’ve spent about 20 minutes of cleanup, plus inspection and LLM prompting, on what’s less than 200 lines of code. I could probably have written the code myself in this time so I feel like it’s a borderline call about whether the LLM is helping at this point.

## Let’s synthesize a raindrop sound

I had an ulterior motive with this entire exercise. I didn’t really want a tone generator. I really wanted to try a raindrop sound synthesizer. I had randomly stumbled across GitHub repository [https://github.com/747745124/Raindrop-Generator](https://github.com/747745124/Raindrop-Generator) and wanted to try the simple waveform it suggested might sound like a raindrop.

![Schematic of the sound produced by a water droplet falling onto a liquid surface. Credit Stanley J. Miklavcic, Andreas Zita and Per Arvidsson](https://www.cocoawithlove.com/assets/blog/raindrop.png)

<sub>Schematic of the sound produced by a water droplet falling onto a liquid surface. Credit [Stanley J. Miklavcic, Andreas Zita and Per Arvidsson](https://www.dafx.de/paper-archive/details/eRUDT2B3rmJZ6w0yVL-fyw)</sub>

Grabbing the “drop_v2.hpp” file from that repository, I asked Copilot to swap the tone generator for a raindrop generator.

> **Prompt:** The samples generated by generateSample in AudioEngine are a basic tone with either a sine, square or sawtooth waveform. Replace this tone generation with a raindrop sample generation. Use the algorithm in drop_v2.hpp for the raindrop sound.

This change broke the compile since it removed a number of parameters that the `ContentView` referenced but after cleaning that up, this step in the exercise was by far the most impressive help that Copilot was able to give.

Ordinarily, when given a new piece of code, in an unfamiliar language and told to integrate the algorithm into an existing codebase, most programmers would need time to process, time to understand and time to feel out the best way to apply.

For an LLM, translating from one context to another is their biggest strength. It’s no problem that one codebase is C++ and the other is Swift. You could argue that all an LLM _ever_ really does is take the pattern and structure of content absorbed in one context and re-emitting that content in a way that follows on from a new context.

However, it’s difficult to tell that this code is working from the audio alone, since it is playing just one 20ms raindrop sound and then stopping.

We’re going to need more drops.

> **Prompt:** The AVAudioSourceNode render function currently plays a single raindrop sound from the rainDrop variable which stops playing once time reaches tInit + deltaT3. This code should be changed so that instead of a single raindrop, there’s an array of raindrops. This array should initially contain just one raindrop but more raindrops should be added to the array after random intervals so that a target number of raindrops are added per minute.

For reasons that are not clear, Copilot ignored the request for “random” and instead the drops are being scheduled precisely `sampleInterval` apart.

After plugging in a rough “random” concept (I don’t think I’ve done a great job, here) and hooking up some sliders to the new `sampleInterval` and `randomness` properties that Copilot has decided to include, the app now looks like this:

![A raindrop synthesizer that actually works](https://www.cocoawithlove.com/assets/blog/raingenerator.png)

<sub>A raindrop synthesizer that actually works</sub>

I’m not sure what that “randomness” parameter is supposed to be. It’s not randomizing the interval between drops and is instead hooked up to a number of internal parameters in a seemingly haphazard way.

## Charting the waveform

The drops sometimes sound like raindrops on a tent, sometimes like small drops in a water glass and often like someone playing a toy xylophone. If nothing else, I’d like to confirm that my waveforms match that in the “A simple water droplet waveform” graph that I showed, above.

To do this, it would be helpful to plot the waveform.

> **Prompt:** I would like to use Swift Charts in the ContentView to show a sample waveform generated by the AudioEngine that updates as the user adjusts the sliders in the ContentView.

This did add a Swift Chart but it showed nothing.

A little inspection revealed that it was plotting the first 1000 samples… of a 44kHz waveform, so just 250 microseconds. Additionally, it was trying to plot all raindrops but I wanted the waveform of a single raindrop.

> **Prompt:** For the generateWaveform function, just generate the waveform from a single raindrop, created locally from the createNewRaindrop function.

Again, some cleanup was needed. I also decided to color code things and hook up sliders to all the key variables (asking Copilot to do this just made a mess).

The end result though is quite nice:

![The waveform of the synthesized raindrop](https://www.cocoawithlove.com/assets/blog/chart-waveform.png)

<sub>The waveform of the synthesized raindrop</sub>

This confirms that the synthesized raindrop is approximately the same as the target waveform.

## Adding some noise

In terms of synthesizing the sound of a raindrop – it’s not great. I can tweak the parameters but it never really sounds like a raindrop and definitely never sounds like rain.

Most people who synthesize rain generally start with a noise generator. There are different types of noise (white, pink, brown). While I know how to write white noise, I’m not sure about brown and don’t have any knowledge of pink noise.

So I make Copilot do it.

> **Prompt:** Add pink noise to the audio generated by the AudioEngine.

```swift
func generatePinkNoise() -> Float {
    let white = Float.random(in: -1.0...1.0)
    pinkNoiseState[0] = 0.99886 * pinkNoiseState[0] + white * 0.0555179
    pinkNoiseState[1] = 0.99332 * pinkNoiseState[1] + white * 0.0750759
    pinkNoiseState[2] = 0.96900 * pinkNoiseState[2] + white * 0.1538520
    pinkNoiseState[3] = 0.86650 * pinkNoiseState[3] + white * 0.3104856
    pinkNoiseState[4] = 0.55000 * pinkNoiseState[4] + white * 0.5329522
    pinkNoiseState[5] = -0.7616 * pinkNoiseState[5] - white * 0.0168980
    let pink = pinkNoiseState[0] + pinkNoiseState[1] + pinkNoiseState[2] + pinkNoiseState[3] + pinkNoiseState[4] + pinkNoiseState[5] + pinkNoiseState[6] + white * 0.5362
    pinkNoiseState[6] = white * 0.115926
    return pink
}
```

It got this right, first time. I think. Honestly, I don’t know what pink noise is supposed to do.

Looking around to see how pink noise generation should look, Copilot appears to have chosen an implementation of the “Voss-McCartney algorithm” for pink noise and [it has a fairly long history](https://www.firstpr.com.au/dsp/pink-noise/).

Further adding brown noise and white noise and hooking up some sliders gives the final form of the app:

![Raindrop and noise generator](https://www.cocoawithlove.com/assets/blog/raingenerator-plusnoise.png)

<sub>Raindrop and noise generator</sub>

## Cleaning up thread safety

It seems that the `AVAudioSourceNode` closure is missing an `@Sendable` annotation so even though Swift 6 doesn’t give any warnings, the code at this point is thread unsafe. In fact, if you annotate `AudioEngine` with `@MainActor`, you’ll get a fatal error at runtime when the render closure is invoked, indicating that Swift 6 is under the (incorrect) assumption that the closure will run in the same context as the surrounding type.

I don’t think there’s anything that would crash the app if the thread safety is left unaddressed – just some parameters that may be invalid or fail to update correctly – but it’s not a good idea to write to the parameters on the main thread and read them from the audio render thread without some form of synchronization.

I asked Copilot to fix the problem:

> **Prompt:** To ensure thread safety in the AudioEngine class, apply these steps:  
>    
>  Add the @MainActor annotation to the AudioEngine class.  
>  Add the @Sendable annotation to the AVAudioSourceNode closure.  
>  Add the nonisolated keyword to the generateAudio function.  
>  Use `Atomic` values to copy parameters from the main actor to the generateAudio function.

Copilot ignored the request for an `@Sendable` annotation and used an `NSLock` instead of `Atomic` so it wasn’t exactly what I wanted. I can’t _really_ fault Copilot since I’m also not sure how to correctly use `Atomic` to solve this problem. In the end, the final commit in this repository (applied manual during a final cleanup phase) adds thread safety via Swift’s new `Mutex` type. I’m not completely happy with that (you don’t generally want to deal with locks on the audio processing thread) but I’m not sure what the best pattern for exchanging data via `Atomic` would be.

## Conclusion

> **Check it out**: the final product plus most of the intermediate steps discussed in this article are available from the [RainGenerator repository](https://github.com/mattgallagher/RainGenerator).

### Is it a good rain synthesizer?

Not really but it was fun to play with, especially once I could see the waveform via the chart.

It turns out that the rough waveform [came from a paper by Stanley J. Miklavcic; Andreas Zita; Per Arvidsson](https://www.dafx.de/paper-archive/details/eRUDT2B3rmJZ6w0yVL-fyw) which goes more into depth about necessary randomization, distribution and spatial effects in order make the raindrops sound more real and even then concludes that other water, flowing and storm sounds are required to fill out the complete soundscape of rain.

### What was Copilot good at?

I asked Copilot to perform a number of refactoring passes and it was generally good at following instructions and cleaning up the integration points. This project is less than 500 lines though, so I don’t know how well it might scale to a more functional sized app.

For SDKs where I wasn’t familiar, it was quicker to give Copilot a vague description of intent than to look up the documentation, read the documentation and integrate into the surrounding context. This is a big win and might help to eliminate the trepidation involved in working with new SDKs.

Copilot was _really_ good at integrating existing code from another location, even when that code was in a different programming language.

It was also _really_ good at looking up how to implement a relatively obscure algorithm like pink noise, even when it’s not an algorithm where the first result in a web search will give a good response.

### Ways in which Copilot was better than expected but not great

I never had a syntax error.

I expected more hallucinations or references to non-existent symbols. I really only experienced one variable that didn’t exist (from the Claude chatbot) and one function that didn’t exist (from Copilot). The non-existant function was `Float.clamped(to: ClosedRange<Float>)` – which I simply implemented as it’s likely just an extension that Copilot has trained on without realizing it’s not a Swift extension.

Other compilation errors I experienced were generally minor (e.g. use of iOS only APIs on the Mac and a use of a variable before the init function had finished initializing) or an update to one file that breaks another file not included in the chat context.

### What was Copilot bad at?

I immediately wanted to make minor changes to almost everything Copilot wrote.

The most common problems were violations of “Don’t repeat yourself”, “Keep it simple, stupid”, missing abstractions or unneeded indirection. Just about every common coding problem was there.

Copilot would repeat code a lot in SwiftUI with the same set of modifiers applied without any desire to avoid repetition. Copilot would also do goofy things like adding `didSet` or `onChange` handlers everywhere instead of simply changing the underlying data without a layer of indirection.

I ended up manually adding `AudioEngine` subtypes – `Raindrop`, `Parameters` and `GeneratorState` – to encapsulate parameters and state and simplify observing and updates because Copilot doesn’t seem to do any such tidy ups without explicit instruction.

As discussed, Copilot left the audio graph incompletely connected, failed to get audio formats aligned between functions. Unless two functions are directly interfacing, it doesn’t seem to check if they’re doing anything related that should be made common.

In some requests, it would outright ignore part of the instructions like “random intervals” or “add @Sendable” to this closure. Other requests like “tidy up the user interface so things are more compact and aligned” don’t seem to have any practical effect (though Copilot might respond by adding a bunch of repetitive modifiers like `onChange` to each slider for no reason).

Copilot never seemed to work out that I was writing a Mac app and kept trying to stick a green background with corner radius inside the Mac “bordered” buttons (really unsightly) and it tried color everything `systemGray6` (I’m not sure why a color should be iOS-only but it is). Perhaps this is my fault for failing to inform the bot about the compile target but it’s just another way you need to work to keep an LLM assistant behaving correctly.

![This Mac button already has a border, and even if this was iOS, that’s probably too much green](https://www.cocoawithlove.com/assets/blog/ugly-green-button.png)

<sub>This Mac button already has a border, and even if this was iOS, that’s probably too much green</sub>

Languages and SDKs evolve pretty quickly and Copilot still seems to prefer `@ObservableObject` over `@Observable` and seems largely unaware of Swift 6, `@Sendable`, `Atomic` and other changes in the last 6 months. You’re limited to its training set and that’s never going to include as much “upcoming” code as “legacy” code.

### Problems with VS Code + Copilot for Swift

Rounding out the negatives are a number of ergonomic problems related to VS Code and its current integration of Copilot.

Any time I manually made changes to the code there’s the problem that this can make the code out-of-sync with the chat window so if you do ask Copilot for more changes, it may behave like your manual changes don’t exist and revert them in its next refactor creating a situation where bugs and entire previous states of the app may reappear.

With code naturally spanning multiple files, it’s easy to forget to include all files in the chat context and have refactoring changes break the connections between two files. What I’d really like is an IDE that automatically detected which files and functions are actually relevant to the context and automatically include them with the request.

And finally, VS Code isn’t Xcode, so it’s not an environment focussed on Swift development. Another developer might be familiar with VS Code but I’m not and I found myself bouncing between IDEs a lot.

### Was Copilot worth it?

Sometimes, yes. But not always and therein lies an estimation risk. Will Copilot write the code I need and save me time? Or will it waste my time as I clean up the mess it makes?

It can be hard to guess whether it would be faster to ask Copilot to improve its own code or to skip Copilot and apply the fix manually. Just typing out a detailed request for changes can take longer than making the changes myself – largely because I’m really accustomed to editing code but I find that being accurate in prose is a slow process. Trying to clean up code details by talking in chat with Copilot can start to feel like a sunk cost problem. Combined with the above-mentioned complication that blending Copilot and manual changes can cause chat to lose sync with the code, it becomes exhausting.

Working with an LLM assistant really does feel like training a very keen but very messy new developer – totally happy to write 1000 lines of code to solve a problem that should be solved in 100 lines and when the PR comes in, you need to slowly walk them through all the things they need to change before you can feel like the code is maintainable.

There is a big difference though: with the new developer, the time taken to help them fix their code isn’t time wasted. They’ll improve, get accustomed to the patterns and expectations of the codebase and in a few months their PRs will be easier to review and they’ll start fixing your dumb mistakes.

By contrast: Copilot is not learning from my suggestions. There’s nothing to be won by making it clean up its own mess if a manual change would have been faster. I’d certainly _like_ Copilot to be better at eliminating redundancy and improving coordination between disparate parts of an app but I can’t make it happen in the short term.
