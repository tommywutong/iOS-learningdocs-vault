---
title: SpeechAnalyzer
framework: Speech
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/speech/speechanalyzer
source_url: 'https://developer.apple.com/documentation/speech/speechanalyzer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/speech/speechanalyzer.json'
content_hash: 'sha256:82b27c740e80417e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Speech](../speech.md)

# SpeechAnalyzer

<sub>Class</sub>

Analyzes spoken audio content in various ways and manages the analysis session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
final actor SpeechAnalyzer
```

## Overview

The Speech framework provides several modules that can be added to an analyzer to provide specific types of analysis and transcription. Many use cases only need a [SpeechTranscriber](speechtranscriber.md) module, which performs speech-to-text transcriptions.

The `SpeechAnalyzer` class is responsible for:

- Holding associated modules
- Accepting audio speech input
- Controlling the overall analysis

Each module is responsible for:

- Providing guidance on acceptable input
- Providing its analysis or transcription output

Analysis is asynchronous. Input, output, and session control are decoupled and typically occur over several different tasks created by you or by the session. In particular, where an Objective-C API might use a delegate to provide results to you, the Swift API’s modules provides their results via an `AsyncSequence`. Similarly, you provide speech input to this API via an `AsyncSequence` you create and populate.

The analyzer can only analyze one input sequence at a time.

### Perform analysis

To perform analysis on audio files and streams, follow these general steps:

1. Create and configure the necessary modules.
2. Ensure the relevant assets are installed or already present. See [AssetInventory](assetinventory.md).
3. Create an input sequence you can use to provide the spoken audio. See helper classes [AssetInputSequenceProvider](assetinputsequenceprovider.md) and [CaptureInputSequenceProvider](captureinputsequenceprovider.md).
4. Create and configure the analyzer with the modules and input sequence.
5. Supply audio. See helper class [AnalyzerInputConverter](analyzerinputconverter.md).
6. Start analysis.
7. Act on results.
8. Finish analysis when desired.

This example shows how you could perform an analysis that transcribes audio using the `SpeechTranscriber` module:

```swift
import Speech

// Step 1: Modules
guard let locale = SpeechTranscriber.supportedLocale(equivalentTo: Locale.current) else {
    /* Note unsupported language */
}
let transcriber = SpeechTranscriber(locale: locale, preset: .transcription)

// Step 2: Assets
if let installationRequest = try await AssetInventory.assetInstallationRequest(supporting: [transcriber]) {
    try await installationRequest.downloadAndInstall()
}

// Step 3: Input sequence
let (inputSequence, inputBuilder) = AsyncStream.makeStream(of: AnalyzerInput.self)

// Step 4: Analyzer
let audioFormat = await SpeechAnalyzer.bestAvailableAudioFormat(compatibleWith: [transcriber])
let analyzer = SpeechAnalyzer(modules: [transcriber])

// Step 5: Supply audio
let converter = AnalyzerInputConverter(analyzerFormat: audioFormat)
Task {
    while /* audio remains */ {
        let buffer = /* Get some audio */
        let inputs = try converter.convert(buffer, at: nil)
        for input in inputs {
            inputBuilder.yield(input)
        }
    }
    let inputs = try converter.flush()
    for input in inputs {
        inputBuilder.yield(input)
    }
    inputBuilder.finish()
}

// Step 7: Act on results
Task {
    do {
        for try await result in transcriber.results {
            let bestTranscription = result.text // an AttributedString
            let plainTextBestTranscription = String(bestTranscription.characters) // a String
            print(plainTextBestTranscription)
        }
    } catch {
        /* Handle error */
    }
}

// Step 6: Perform analysis
let lastSampleTime = try await analyzer.analyzeSequence(inputSequence)

// Step 8: Finish analysis
if let lastSampleTime {
    try await analyzer.finalizeAndFinish(through: lastSampleTime)
} else {
    try analyzer.cancelAndFinishNow()
}
```

### Analyze audio from files or capture devices

To read audio from a file, asset, or capture device such as a microphone, create an [AssetInputSequenceProvider](assetinputsequenceprovider.md) or [CaptureInputSequenceProvider](captureinputsequenceprovider.md) object.

Get the provider object’s [analyzerInputs](assetinputsequenceprovider/analyzerinputs.md) or [analyzerInputs](captureinputsequenceprovider/analyzerinputs.md) property to convert the source’s audio to a supported format and obtain an asynchronous input sequence of the audio. Pass that sequence to [analyzeSequence(_:)](<speechanalyzer/analyzesequence(__).md>), [start(inputSequence:)](<speechanalyzer/start(inputsequence_).md>), or a similar parameter of the analyzer’s initializer.

To end the analysis session after processing the audio track or captured audio, call one of the analyzer’s `finish` methods. Otherwise, by default, the analyzer won’t terminate its result streams and will wait for additional audio input sequences or buffers. See the “Finish analysis” section below for more details.

### Analyze audio from audio buffers

You can analyze audio buffers directly without using [AssetInputSequenceProvider](assetinputsequenceprovider.md) or [CaptureInputSequenceProvider](captureinputsequenceprovider.md).

To do this:

1. Create an asynchronous input sequence of [AnalyzerInput](analyzerinput.md) elements that is appropriate for your use case.
2. Supply the input sequence to [analyzeSequence(_:)](<speechanalyzer/analyzesequence(__).md>), [start(inputSequence:)](<speechanalyzer/start(inputsequence_).md>), or a similar parameter of the analyzer’s initializer.
3. Convert each audio buffer to a supported audio format, either on the fly or in advance.
4. Create [AnalyzerInput](analyzerinput.md) objects for each buffer.
5. Add the `AnalyzerInput` objects to the input sequence.

To convert `AVAudioBuffer` audio buffers to a supported format as `AnalyzerInput` objects on the fly, use [AnalyzerInputConverter](analyzerinputconverter.md).

To convert audio buffers to a supported format in advance or with some other technique:

1. Detemine the format to convert to by calling [bestAvailableAudioFormat(compatibleWith:)](<speechanalyzer/bestavailableaudioformat(compatiblewith_).md>) or individual modules’ [availableCompatibleAudioFormats](speechmodule/availablecompatibleaudioformats.md) methods
2. Convert the audio and create `AnalyzerInput` objects as necessary

To skip past part of an audio stream, omit the buffers you want to skip from the input sequence. You can resume with a later buffer.

When you resume analysis with a later `AVAudioPCMBuffer` buffer, you may need to supply the correct time-code to account for skipped audio. To do this, pass the time-code of the later buffer as the `bufferStartTime` parameter of the corresponding `AnalyzerInput` object.

### Analyze autonomously

You can and usually should perform analysis using the [analyzeSequence(_:)](<speechanalyzer/analyzesequence(__).md>) or [analyzeSequence(from:)](<speechanalyzer/analyzesequence(from_).md>) methods; those methods work well with Swift structured concurrency techniques. However, you may prefer that the analyzer proceed independently and perform its analysis autonomously as audio input becomes available in a task managed by the analyzer itself.

To use this capability, create the analyzer with one of the initializers that has an input sequence or file parameter, or call [start(inputSequence:)](<speechanalyzer/start(inputsequence_).md>) or [start(inputAudioFile:finishAfterFile:)](<speechanalyzer/start(inputaudiofile_finishafterfile_).md>). To end the analysis of that input only and start analysis of different input, call one of the `start` methods again. To end the analysis session when the input ends, call [finalizeAndFinishThroughEndOfInput()](<speechanalyzer/finalizeandfinishthroughendofinput().md>).

### Control processing and timing of results

Modules deliver results periodically, but you can manually synchronize their processing and delivery to outside cues.

To deliver a result for a particular time-code, call [finalize(through:)](<speechanalyzer/finalize(through_).md>). To cancel processing of results that are no longer of interest, call [cancelAnalysis(before:)](<speechanalyzer/cancelanalysis(before_).md>).

### Improve responsiveness

By default, the analyzer and modules load the system resources that they require lazily, and unload those resources when they’re deallocated.

To proactively load system resources and “preheat” the analyzer, call [prepareToAnalyze(in:)](<speechanalyzer/preparetoanalyze(in_).md>) after setting its modules. This may improve how quickly the modules return their first results.

To delay or prevent unloading an analyzer’s resources — caching them for later use by a different analyzer instance — you can select a [ModelRetention](speechanalyzer/options/modelretention-swift.enum.md) option and create the analyzer with an appropriate [Options](speechanalyzer/options.md) object.

To set the priority of analysis work, create the analyzer with a [Options](speechanalyzer/options.md) object with the desired `priority` value.

Specific modules may also offer options that improve responsiveness.

### Finish analysis

To end an analysis session, you must use one of the analyzer’s `finish` methods or parameters, or deallocate the analyzer.

When the analysis session transitions to the _finished_ state:

- The analyzer won’t consume additional input from the input sequence (but note that it doesn’t drain or terminate the sequence)
- Most methods won’t do anything; in particular, the analyzer won’t accept different input sequences or modules
- Module result streams terminate and modules won’t publish additional results, though the app can continue to iterate over already-published results

> [!note] Note
> While you can terminate the input sequence you created with a method such as `AsyncStream.Continuation.finish()`, terminating the input sequence does _not_ generally finish the analysis session, and you can continue the session with a different input sequence. (See [finalizeAndFinishThroughEndOfInput()](<speechanalyzer/finalizeandfinishthroughendofinput().md>) for an exception.)

### Respond to errors

When the analyzer or its modules’ result streams throw an error, the analysis session becomes finished as described above, and the same error (or a `CancellationError`) is thrown from all waiting methods and result streams.

When this happens, you may wish to terminate the input sequence, or create a new analyzer to continue working on the remaining (and any additional) input.

### Manage simultaneous analyses

The system normally limits simultaneous analyses to a conservative number, considering hardware capabilities of different devices. If you exceed that number, the system throws an [insufficientResources](sfspeecherror/code/insufficientresources.md) error.

However, under certain use cases, the hardware may be able to accommodate additional simultaneous analyses; for example, several simultaneous transcription sessions may use the same language and settings, or only receive audio in an interleaved schedule. To support these use cases, you can override the system to ignore the predefined conservative system resource limits.

To override the normal limits, create an analyzer with a [Options](speechanalyzer/options.md) object with its [ignoresResourceLimits](speechanalyzer/options/ignoresresourcelimits.md) value set to `true`. The system allows an unlimited number of analyzers configured with this option. However, the hardware requirements of numerous analyzers will eventually exceed the system’s actual capacity, and one or more of the analyzers will fail, throwing an unpredictable error.

> [!warning] Warning
> When using this option, test your app on a variety of devices under a variety of scenarios to experimentally determine how many analyzers you can reliably create and expect to function. Consider how to recover in the event one or more analyzers fail.

## Relationships

- **Conforms To**: [Actor](../swift/actor.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an analyzer

- [init(modules:options:)](<speechanalyzer/init(modules_options_).md>) — Creates an analyzer.
- [init(inputSequence:modules:options:analysisContext:volatileRangeChangedHandler:)](<speechanalyzer/init(inputsequence_modules_options_analysiscontext_volatilerangechangedhandler_).md>) — Creates an analyzer and begins analysis.
- [init(inputAudioFile:modules:options:analysisContext:finishAfterFile:volatileRangeChangedHandler:)](<speechanalyzer/init(inputaudiofile_modules_options_analysiscontext_finishafterfile_volatilerangechangedhandler_).md>) — Creates an analyzer and begins analysis on an audio file.
- [Options](speechanalyzer/options.md) — Analysis processing options.

### Managing modules

- [setModules(_:)](<speechanalyzer/setmodules(__).md>) — Adds or removes modules.
- [modules](speechanalyzer/modules.md) — The modules performing analysis on the audio input.

### Performing analysis

- [analyzeSequence(_:)](<speechanalyzer/analyzesequence(__).md>) — Analyzes an input sequence, returning when the sequence terminates.
- [analyzeSequence(from:)](<speechanalyzer/analyzesequence(from_).md>) — Analyzes an input sequence created from an audio file, returning when the file has been read.

### Performing autonomous analysis

- [start(inputSequence:)](<speechanalyzer/start(inputsequence_).md>) — Starts analysis of an input sequence and returns immediately.
- [start(inputAudioFile:finishAfterFile:)](<speechanalyzer/start(inputaudiofile_finishafterfile_).md>) — Starts analysis of an input sequence created from an audio file and returns immediately.

### Finalizing and cancelling results

- [cancelAnalysis(before:)](<speechanalyzer/cancelanalysis(before_).md>) — Stops analyzing audio predating the given time.
- [finalize(through:)](<speechanalyzer/finalize(through_).md>) — Finalizes the modules’ analyses.

### Finishing analysis

- [cancelAndFinishNow()](<speechanalyzer/cancelandfinishnow().md>) — Finishes analysis immediately.
- [finalizeAndFinishThroughEndOfInput()](<speechanalyzer/finalizeandfinishthroughendofinput().md>) — Finishes analysis after an audio input sequence has been terminated and fully consumed and the modules’ results are finalized.
- [finalizeAndFinish(through:)](<speechanalyzer/finalizeandfinish(through_).md>) — Finishes analysis after finalizing results for a given time-code.
- [finish(after:)](<speechanalyzer/finish(after_).md>) — Finishes analysis once input for a given time is consumed.

### Determining audio formats

- [bestAvailableAudioFormat(compatibleWith:)](<speechanalyzer/bestavailableaudioformat(compatiblewith_).md>) — Retrieves the best-quality audio format that the specified modules can work with, from assets installed on the device.
- [bestAvailableAudioFormat(compatibleWith:considering:)](<speechanalyzer/bestavailableaudioformat(compatiblewith_considering_).md>) — Retrieves the best-quality audio format that the specified modules can work with, taking into account the natural format of the audio and assets installed on the device.

### Improving responsiveness

- [prepareToAnalyze(in:)](<speechanalyzer/preparetoanalyze(in_).md>) — Prepares the analyzer to begin work with minimal startup delay.
- [prepareToAnalyze(in:withProgressReadyHandler:)](<speechanalyzer/preparetoanalyze(in_withprogressreadyhandler_).md>) — Prepares the analyzer to begin work with minimal startup delay, reporting the progress of that preparation.

### Monitoring analysis

- [setVolatileRangeChangedHandler(_:)](<speechanalyzer/setvolatilerangechangedhandler(__).md>) — A closure that the analyzer calls when the volatile range changes.
- [volatileRange](speechanalyzer/volatilerange.md) — The range of results that can change.

### Managing contexts

- [setContext(_:)](<speechanalyzer/setcontext(__).md>) — Sets contextual information to improve or inform the analysis.
- [context](speechanalyzer/context.md) — An object containing contextual information.

## See Also

### Essentials

- [Speech updates](../updates/speech.md) — Learn about important changes to Speech.
- [Recognizing speech in live audio](recognizing-speech-in-live-audio.md) — Perform speech recognition and transcription on audio captured from the microphone of an iOS device.
- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md) — Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [AssetInventory](assetinventory.md) — Manages the assets that are necessary for transcription or other analyses.
