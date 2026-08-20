---
title: Core Audio Glossary
apple_id: TP40004453
resource_type: Guide
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2010-08-30'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CoreAudioGlossary/Glossary/core_audio_glossary.html
archived_at: '2026-07-15T08:18:03.374825Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Audio Glossary](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

# Glossary

- __5.1 Surround Sound__

  A surround sound speaker configuration consisting of five speakers arranged in specific positions along the circumference of a circle, and a subwoofer (the “.1”). The speaker channels are typically designated as follows: left, center, right, left surround. right surround, and LFE (low frequency effect).

- __8.24__

  Sometimes written as _Q8.24_ or _fx8.24_. A [fixed-point sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzg4) size used as the canonical audio sample type for processing [linear PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbduqrsk) audio in iOS, in lieu of 32-bit floating point samples. In an 8.24 audio sample there are eight bits to the left of the radix point, forming the integer (or “magnitude”) portion of the value, and 24 bits to the right, forming the fractional portion.

- 
  __AAC (Advanced Audio Coding)__

  A compressed, lossy, [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuha) scheme, originally a component of the MPEG-2 standard as MPEG-2 AAC. Defined in 1997 as part of ISO/IEC 13818-7. Enhanced for the MPEG-4 standard as MPEG-4 AAC. MPEG-2 AAC provides better perceived audio quality at the same bit rate compared to MPEG-1, layer 3 ([MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuhe)), according to results published in ISO/IEC JTC1/SC29/WG11, N2006 (February 1998). MPEG-4 AAC extends MPEG-2 AAC with additional coding tools. See also [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkinaukq2b).

- __AC-3__

  A compressed, lossy, perceptual audio coding format developed by Dolby Laboratories, Inc. Sometimes called _Dolby Digital_ or _Dolby Surround AC-3_. See also [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkinaukq2b), [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi).

- __active__

  In iOS, used to describe an [audio session](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrhazq) state in which playback or recording can proceed. Compare [inactive](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha3a).

- __ADC (analog-to-digital converter)__

  Circuitry that converts analog signals to corresponding digital code using sampling and quantization. ADCs are characterized by sample rate, amplitude resolution in terms of bit depth, quantization error and other distortion characteristics, and noise floor. Professional audio work usually employs ADCs with a linear response. Compare [DAC (digital-to-analog converter)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbduqqkd). See also [quantization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbegssk), [sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdecrsh).

- __ADPCM (adaptive delta pulse code modulation)__

  A variant of [pulse-code modulation (PCM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdeuskg), and an extension of [DPCM (differential pulse code modulation)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxha), that varies quantization step size to minimize bit rate for a given dynamic range.

- __AES (Audio Engineering Society)__

  An international society of audio professionals that has established many important standards related to digital audio.

- __AES-3__

  A digital audio transport standard defined by the Audio Engineering Society, originally published in 1992. Also called the _AES/EBU interface_. Equivalent to IEC 60958 Part 4. The AES-3 standard includes parts for various physical connections including balanced twisted-pair wire, unbalanced coaxial cable, and optical fiber. The technical inspiration for AES-3 was the [S/PDIF (Sony/Phillips Digital Interface)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzshe) standard.

- __AES/EBU interface__

  An alternate name for [AES-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztga). See also [EBU (European Broadcasting Union)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgi).

- __aggregate device__

  A set of two or more audio devices interconnected to allow the set to be addressed by software applications as a single device. See also [device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5cemrkg).

- __AIFF (Audio Interchange File Format)__

  A digital audio file format developed by Apple, Inc., based on the Interchange File Format (IFF) developed by Electronic Arts, Inc. The audio data in an AIFF file is uncompressed, big-endian PCM and is stored in chunks. See also [chunk](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijfeeqsd), [linear PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbduqrsk).

- __AIFC (Audio Interchange File Format Extension for Compression)__

  An extension of AIFF that supports storage of either compressed or uncompressed audio data. May also be abbreviated as _AIFF-C_. With the availability of newer audio compression schemes such as MP3 and AAC, AIFC is rarely used. It is still supported in OS X.

- __aliasing__

  Distortion resulting from sampling a signal containing energy at or above the [Nyquist frequency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgq). In audio, aliasing results in artifacts below the Nyquist frequency, sometimes called _aliasing distortion_. To avoid aliasing, audio signals must be low-pass filtered to remove energy at or above the Nyquist frequency before sampling.

- __Anatomical Transfer Function__

  See [HRTF (head related transfer function)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgy).

- __Apple Core Audio Format__

  Apple’s universal audio file format. Apple Core Audio Format is sometimes called _Core Audio Format_ or _CAF_. CAF files are chunk-based and can contain AAC, MP3, and PCM audio data, among many other audio data formats, as well as MIDI data. See also [chunk](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijfeeqsd), [pulse-code modulation (PCM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdeuskg).

- __Apple Lossless__

  A compressed, lossless digital audio encoding format defined by Apple, Inc. See also [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizduqssb).

- __asynchronous__

  In Audio Queue Services, describes one of two ways to stop an audio queue. Asynchronous stopping happens after all queued buffers have been played or recorded. In digital communications, a transmission method that does not require the clock frequency of the sender and receiver to be the same. Compare [synchronous](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwge).

- __ATF (Anatomical Transfer Function)__

  See [HRTF (head related transfer function)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgy).

- __audio file stream__

  In Core Audio, a software object of type `AudioFileStreamID`, which represents data obtained from a TCP stream and supports manipulation of that data. See also [TCP (Transmission Control Protocol) stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgm).

- __audio processing graph__

  A representation of a signal chain comprising an interconnection of audio units. Also called an _AUGraph_ or _graph_. Core Audio represents such an interconnected network as a software object of type`AUGraph`. Audio processing graphs must end in an [output unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyg4). See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi).

- __audio queue__

  In Audio Queue Services, a software object of type `AudioQueueRef`, used for recording or playing back audio. There are two distinct types of audio queue. A recording (sometimes called _input_) audio queue typically accepts incoming audio from a hardware device and uses a callback function on its output side. A playback (sometimes called _output_) audio queue has a callback on its input side, and typically sends its output audio to external hardware.

- __audio queue buffer__

  In Audio Queue Services, a data structure used as a container for transient blocks of audio data being played or recorded. An audio queue buffer is managed by the [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgu) that owns it.

- __audio session__

  An iOS software abstraction that represents audio behavior for an application, in context with other applications, when running on a device. An audio session has a [category](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha2a) and can be [active](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha2q) or [inactive](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha3a).

- __audio session category__

  See [category](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha2a).

- __audio unit__

  A Component Manager–based [plug-in](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfcusrch) that adds an audio feature to a Mac app. Audio units can provide effects such as filtering and reverb, MIDI-based music synthesis, audio data format conversions, mixing, panning, sound generation, and audio playback. Unlike application-specific plug-ins, audio units are available systemwide. Multiple instances of a single audio unit can run simultaneously.

- __AUGraph__

  See [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzu).

- __AUHAL__

  An Apple-supplied [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) used to interface with hardware input or output, so named because it interacts with the [Hardware Abstraction Layer (HAL)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceireeeq2c).

- __AV/C (Audio/Video Control)__

  The AV/C standard, published by the [IEEE (Institute of Electrical and Electronic Engineers)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizbuuqsk), provides a music and audio device command protocol over [FireWire](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgu) (IEEE 1394) connections.

- __average bit rate__

  Describes an encoded audio representation that, while allowing variations in bit rate from frame to frame, maintains a specific average bit rate over a long time interval (typically between 10 and 60 seconds). You can use ABR-savvy encoders to fit a recording into a predetermined file size. Compare [constant bit rate (CBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztha), [variable bit rate (VBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgm).

- __AVI (Audio Video Interleave)__

  A chunk-based, container file format defined by Microsoft Corporation in 1992. AVI is a specialization of the [RIFF (Resource Interchange File Format)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivduoqsf) format, which in turn is based on [IFF (Interchange File Format)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdeersd).

- __azimuth__

  In [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxg4) and [immersive audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyha), the real or apparent horizontal angle of an audio source referenced to a line drawn from the listener’s head to a point directly ahead of the listener.

- __bandwidth__

  1. In analog audio, the width of a frequency band for a [transmission channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgu), from a lower to an upper frequency limit. The limits are defined in terms of signal attenuation, in decibels, relative to the level at the center of the band. See also [decibel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijausscb). 2. In digital data transmission, the available data throughput for a transmission channel. Digital bandwidth is typically expressed in terms of bits or bytes per second. See also [bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceirdessse).

- __beat__

  The basic time unit of a musical piece; typically, the bottom number in a time signature. Core Audio’s [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzz) uses the notion of beats in the tempo track.

- __bit depth__

  Sample resolution; the number of bits per sample. Along with some other factors, bit depth determines the [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizaueqkd) of a digital system.

- __bit rate__

  The data rate (or [bandwidth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjeugr2i)) of a digital channel, in bits per second.

- __buffer__

  Memory assigned to temporarily hold data between a source and a destination. For example, Core Audio uses buffers to supply audio to, and receive audio from, audio units. See also [audio queue buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxge).

- __buffer queue__

  In Audio Queue Services, an ordered list of audio queue buffers used by an audio queue. See also [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgu), [audio queue buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxge).

- __bus__

  See [element](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkjjcugscb).

- __CAF__

  See [Apple Core Audio Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceinceqscc).

- __category__

  Also called _audio session category_. In iOS, a collection of audio behaviors for an application. For example, a category specifies whether an application intends to mix its audio with other applications or silence them. You specify your application’s category after initializing its audio session.

- __CBR__

  See [constant bit rate (CBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztha).

- __ceiling__

  The maximum allowable signal level in an audio system. The ratio of the ceiling to the [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijdeqssc) is the [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha). Also called _dynamic ceiling_.

- __channel__

  A discrete track of audio. A monaural recording or live performance has exactly one channel. A stereo recording or live performance has two channels. A multitrack recording or performance can have any number of channels. Between audio units, a [connection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuga) has one or more channels. See also [channel layout](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfcuerkh).

- __channel layout__

  A description of the playback roles for the channels in an audio recording. For example, in a stereo recording, channel 1 has the role of “left front” and channel 2 has the role of “right front.”

- __chunk__

  A linear block of data consisting of a short, descriptive header followed by the described data. A chunk-based file is an on-disk file laid out as a series of chunks.

- __chunk header__

  The descriptive, metadata section at the start of a [chunk](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijfeeqsd). Each element of information in a chunk header is called a _field_.

- __chunk data section__

  The data content of a [chunk](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijfeeqsd). The format of the data depends on the chunk type, as specified in the chunk header.

- __clipping__

  Distortion of a [waveform](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceineugr2k) resulting from the limiting of signal amplitude to a specific level. See also [distortion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5cuiskc).

- __clock__

  The regular, periodic signal in a digital audio system used to pace audio recording and playback.

- __clock drift__

  The deviation, over time, of one [clock](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfduqski) relative to another, due to differing counting rates. Clock drift interferes with synchronization.

- __clock recovery__

  Extracting and reconstructing timing information from a data stream.

- __codec (coder/decoder)__

  A generic term applied to, among other things, lossy and lossless audio compression technologies implemented in hardware or software. Encoded data can be wrapped in a file format appropriate for the data, or decoded from such a file format. For example, the MP3 file format is a wrapper that can hold perceptually-encoded audio data.

- __component__

  In OS X, a plug-in whose interface is defined by the Component Manager. An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) is a component.

- __compression__

  See [data compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvga), [level compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvge).

- __compressor__

  Hardware or software that implements either [data compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvga) or [level compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvge). A data compressor, along with its corresponding decompressor, is sometimes referred to as a _codec_.

- __connection__

  In Core Audio, a hand-off point for audio data entering or leaving an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi). A connection has one or more channels. See also [channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzthe).

- __constant bit rate (CBR)__

  A data encoding scheme that can be used to stream audio data over a channel at a constant bit rate while supporting real-time decoding. In most cases, packet size is constant in CBR streams. In the case of constant bit rate AAC streams, packet size may vary slightly. Some encoding schemes, such as PCM, support only CBR encoding. Compare [average bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzugy), [variable bit rate (VBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgm). See also [packet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfduuscc).

- __cookie__

  See [magic cookie](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvha).

- __coordinate scale__

  In Core Audio, for a [panner unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygq), a parameter that specifies the maximum value for the distance parameter, in meters.

- __Core Audio__

  A set of iOS and OS X frameworks that provides audio services (depending on the platform) that include recording, playback, synchronization, signal processing, format conversion, panning and surround sound, hardware abstraction, and others.

- __Core Audio Format__

  See [Apple Core Audio Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceinceqscc).

- __Core MIDI__

  An OS X framework for controlling and communicating with MIDI devices.

- __DAC (digital-to-analog converter)__

  Circuitry that converts digital data to a corresponding analog signal. DACs are characterized by maximum sampling frequency, amplitude resolution in terms of bit depth, monotonicity, distortion characteristics, and noise floor. Compare [ADC (analog-to-digital converter)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfbekssd).

- __data compression__

  Algorithmic reduction of data size to improve storage or transmission efficiency. Data compression can be lossy or lossless. Compression is a special case of [encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijduescb). See also [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizduqssb), [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkinaukq2b), [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi).

- __dB__

  See [decibel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijausscb).

- __dBu__

  An absolute measure of RMS voltage level in decibels relative to 0.775 Volts RMS. dBu measurements assume a circuit load with infinite impedance. See also [RMS (root mean square)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzugu).

- __decibel__

  A dimensionless unit for expressing the ratio of two quantities, abbreviated as _dB_. The decibel difference between two power levels is equal to 10 times the common logarithm of their ratio. The decibel difference between two voltage levels is equal to 20 times the common logarithm of their ratio. Decibel values are typically associated with a standard voltage or power level. For example, acoustic levels are commonly referenced to 0 dB SPL, equivalent to 20 µPa (micropascals). See also [SPL (sound pressure level)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvgy).

- __decode__

  To retrieve the original signal from an encoded representation of it. For lossy encoding schemes such as MP3, the retrieved signal approximates the original signal. See also [codec (coder/decoder)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkcjbeuqqkb), [encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijduescb).

- __default output unit__

  An Apple-supplied [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) that connects with whichever hardware device the user has designated to be the default output.

- __deinterleaving__

  A synonym for _reverse multiplexing_. In digital audio , retrieving discrete channels from an interleaved representation. Compare [interleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjcuirse).

- __delay__

  The time lag between one audio event and another. In audio processing, the second event is typically a processed or unprocessed copy of the original event. Delay is a settable [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5aukr2j) in the AUDelay [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) included in OS X.

- __device__

  In audio generally, a piece of equipment or a software entity that produces, transforms, transmits, receives, or stores audio data. In MIDI, a piece of equipment or a software entity that responds to MIDI control or provides MIDI data. In Audio Queue Services, a source or destination for audio, such as a microphone or a loudspeaker.

- __digital rights management (DRM)__

  A generic term referring to embedded, electronic restriction over the use of electronic content. Usually applied to copyrighted material. See also [FairPlay](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbfesskk).

- __digital signal processing (DSP)__

  In audio, analyzing or transforming digital representations of audio. Such transformations include, among others, filtering and equalization, reverberation, level compression, data compression, and sound effects such as pitch shifting. Digital signal processing can be performed by hardware, software, or a combination of both.

- __discontinuity__

  In an audio data stream, a distinct break in the sequence of transmitted data. A discontinuity entails a period in which the stream is undefined. See also [TCP (Transmission Control Protocol) stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgm).

- __distance__

  In [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxg4) and immersive audio, the real or apparent straight line distance of an audio source from the listener.

- __distortion__

  A difference, typically unintentional and undesired, between the signals on the input and output of an audio device. Commonly measured types of distortion include harmonic distortion, intermodulation distortion, quantization distortion, and jitter. Intentional differences between input and output signals, such as level or equalization differences, are not described as distortion. Compare [noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbbuissj).

- __dither__

  Low-amplitude noise applied to a signal to reduce quantization error. See also [quantization noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrhe).

- __DPCM (differential pulse code modulation)__

  A variant of [pulse-code modulation (PCM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdeuskg) that encodes the difference between the current and previous sample.

- __DRM__

  See [digital rights management (DRM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbduurse).

- __DSP__

  See [digital signal processing (DSP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbuesce).

- __dynamic range__

  A quality measure for an audio device or system that describes the difference between the loudest and softest signal that can appear at the output of the device. Dynamic range is equal to the ratio of dynamic ceiling to noise floor, typically described in decibels. See also [ceiling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfdemqsk), [decibel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijausscb),[noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijdeqssc).

- __EBU (European Broadcasting Union)__

  A Europe-based, international, audio and broadcasting standards organization.

- __effect unit__

  In Core Audio, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) of type `'aufx'` that employs DSP to modify a stream of digital audio. See also [digital signal processing (DSP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbuesce).

- __element__

  In Core Audio, an audio unit programming context nested within a scope. When part of an input or output scope of an audio unit, an element is analogous to a device signal bus—and is sometimes called a _bus_. See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi), [scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsscirausr2k).

- __elevation__

  In [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxg4) and [immersive audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyha), the real or apparent vertical angle of an audio source referenced to a line drawn from a listener’s head to a point directly ahead of the listener.

- __encoding__

  Algorithmic conversion of a signal from one representation to another. For example, compressing linear PCM data to AAC format is a form of encoding. Can be applied to perceptual or lossless data compression. See also [codec (coder/decoder)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkcjbeuqqkb), [decode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5ceoq2d). Compare [data compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvga).

- __endpoint__

  See [MIDI endpoint](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgq).

- __entity__

  See [MIDI entity](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzs).

- __event track__

  A stream of MIDI or event data which can be played using a [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzz). See also [sequence](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrge).

- __externally framed__

  Describes a [variable bit rate (VBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgm) audio format where information about the sizes of the frames is transmitted separately from the audio data stream. Compare [internally framed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsge). See also [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgi).

- __factory preset__

  See [preset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrguya).

- __FairPlay__

  The [digital rights management (DRM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbduurse) system built into Apple’s QuickTime technology and used by the iPod music player, the iTunes music application, and the iTunes store. These systems use FairPlay to encrypt some AAC files to restrict their playback to authorized devices.

- __fan out__

  In electronics generally, to direct one output signal to multiple inputs. Audio units cannot perform fan out of this sort. To feed multiple [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) inputs, you direct an audio unit output to a buffer (such as a splitter unit) that has multiple outputs, each of which can connect to a separate audio unit input.

- __FireWire__

  Apple’s implementation of the IEEE 1394 standard serial bus for connecting digital devices such as cameras and hard drives.

- __fixed-point sample__

  A digital audio [sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdecrsh) that uses a fixed-point numerical representation, such as [8.24](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzha). Fixed-point samples support fixed-point arithmetic, which is a less computation-intensive alternative to floating-point arithmetic.

- __frame__

  In Core Audio, a set of samples that contains one sample from each channel in an audio data stream. In the most common case, the samples in a frame are time-coincident—that is, sampled at the same moment. For example, in a stereo stream each frame contains one sample from the left channel and a time-coincident sample from the right channel. More generally, the various channels in a stream, and therefore in a frame, may be from unrelated sources and may have originated at unrelated times. In video, a single image in a series that constitutes a movie. See also [packet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfduuscc).

- __frame rate__

  In Core Audio, the number of frames played per second for an audio data stream. Compare [sample rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivbukrch). In video playback, the number of video frames displayed per second.

- __frequency__

  The number of times a repeating phenomenon or activity occurs per unit time. The frequency of a sound wave is determined by the number of wavelengths (or fractions thereof) that pass a particular point per unit time. Sampling frequency indicates the number of digital samples taken per unit time. Frequency is typically measured in Hertz (cycles per second).

- __gain__

  The ratio of output level to the corresponding input level for a device. Level is typically represented in terms of power or voltage, but gain is unitless and is identical whether voltages or powers were used to calculate it. Because gain is a ratio, it is usually described using decibels. A gain of 0 dB indicates no change in level, while a gain of 10 dB is perceived as approximately a doubling in loudness—depending on the nature of the sound and on the initial loudness.

- __graph__

  See [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzu).

- __HAL__

  See [Hardware Abstraction Layer (HAL)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceireeeq2c).

- __Hardware Abstraction Layer (HAL)__

  An object-like interface between Core Audio objects and hardware. The hardware abstraction layer typically addresses hardware by means of an I/O Kit driver, but this is not a requirement. The HAL gives applications a consistent way to communicate with external devices—insulating them from the complexity of addressing multiple, specialized hardware drivers.

- __head node__

  The final node in an [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzu) in terms of signal flow; the output node of a graph. See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi), [node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyhe).

- __Head Related Transfer Function__

  See [HRTF (head related transfer function)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgy).

- __headroom__

  The range, expressed in decibels, between a standard reference signal level and the maximum allowable signal level (the ceiling). See also [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha).

- __host application__

  A Mac app that loads and uses audio units. See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi).

- __host time__

  The clock time used by the computer running an audio application.

- __HRTF (head related transfer function)__

  Also called _Anatomical Transfer Function_, or _ATF_. A mathematical description of the frequency and phase filtering that takes place when an acoustic signal impinges on a person’s head and pinnae. The HRTF is used in DSP to add spatialization information to a signal. See also [digital signal processing (DSP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbuesce),[panning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwga), [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgq).

- __IEC (International Electrotechnical Commission)__

  An international standards organization, founded in 1906, that collaborates with [ISO (International Organization for Standardization)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizeeer2d) on defining a wide variety of [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi) formats.

- __IEEE (Institute of Electrical and Electronic Engineers)__

  An organization of electronics professionals that has established many technology and audio-related standards. Pronounced “eye triple-e.”

- __IEEE 1394__

  See [FireWire](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgu).

- __IFF (Interchange File Format)__

  A flexible, chunk-based file format for storing media content. Developed by Electronic Arts, Inc., and the technical inspiration for Apple’s [AIFF (Audio Interchange File Format)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvgu).

- __IMA ADPCM__

  IMA is the abbreviation for _Interactive Multimedia Association_. A lossy, 16-bit audio compression format that provides 4:1 compression. The format is sometimes referred to as _IMA_ or _IMA4_. See also [ADPCM (adaptive delta pulse code modulation)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxhe).

- __immersive audio__

  Sound reproduction or generation that seems to surround a listener. See also [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxg4).

- __impedance__

  In electronics, the amount of opposition a circuit presents to an AC (alternating current) signal at a given frequency. Impedance includes both a resistive (frequency-independent) and a reactive (frequency-dependent) component. In acoustics, the ratio of average sound pressure to particle velocity over a given surface area and at a given frequency.

- __inactive__

  In iOS, used to describe an audio session state in which playback or recording cannot proceed. Compare [active](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha2q).

- __initialize__

  In Core Audio, to configure an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) for use.

- __input audio queue__

  Also called _recording audio queue_. See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgu).

- __instrument unit__

  In Core Audio, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) of type `'aumu'` that takes sound bank data and MIDI control data as inputs, and outputs digital audio.

- __interleaving__

  A synonym for _multiplexing_. In digital audio, converting a set of data streams representing discrete channels into a single stream that retains the capacity to be converted back to separate channels. In Audio Converter Services and in audio file formats such as CAF, interleaving involves placing one [sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdecrsh) from each channel in sequence such that a set of coincident samples, one from each channel represented in the data stream, appears in each frame. Compare [deinterleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijceer2g).

- __internally framed__

  Describes a variable-bit-rate audio format where information about the sizes of the frames is included in the audio data stream. Compare [externally framed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgm). See also [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgi), [variable bit rate (VBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgm).

- __I/O (input/output)__

  A generic term for the software- or hardware-based audio inputs and outputs for a device. Pronounced “eye-oh.”

- __ISO (International Organization for Standardization)__

  ISO, based in Geneva, Switzerland, collaborates with the [IEC (International Electrotechnical Commission)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbegrcj) on defining a wide variety of [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi) formats. Pronounced “EYE-so.”

- __jitter__

  Time-based inconsistencies in the clock signal or clock component in a digital signal stream. In digital audio, jitter can result in audible [distortion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5cuiskc).

- __latency__

  In digital audio processing, the time required for an audio sample to proceed from an input to a corresponding output. Total latency, depending on the scope of the system under consideration, can include unavoidable hardware latency (sometimes called _I/O latency_), safety offset latency (required for robust driver operation), and buffer latency (typically software controlled; dependent on digital signal processing requirements).

- __leading frames__

  In audio data format conversion, frames of audio data that precede, in time, the nominal starting frame for an input [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgq). See also [priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuge). Compare [trailing frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrheya).

- __level__

  A description of the nominal audio signal strength resulting from a given input level and gain in an audio device or system. Level within analog audio circuitry is often measured in dBu. The instantaneous signal strength, for any nominal level, can vary from the noise floor to the dynamic ceiling. Professional “line level” typically indicates a nominal level of +4 dBu, while “consumer level” typically indicates a nominal level of –10 dBu. See also [ceiling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfdemqsk),[dBu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivbuisck), [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijdeqssc). Compare [volume](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvhe).

- __level compression__

  Reduction of the dynamic range of an audio signal, typically by reducing the gain ratio for amplitudes above a specific level. Compare [limiting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjdeoscb).

- __LFE (low frequency effect)__

  One of the six typical channels in [5.1 Surround Sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwha). The LFE channel covers the bottom two or three octaves of audio and is typically used to enhance the realism of sound effects such as explosions.

- __limiter__

  Circuitry or software that limits signal amplitude to a user-defined maximum. Compare [level compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvge).

- __limiting__

  The process of preventing signal amplitude from exceeding a user-defined maximum.

- __linear__

  Describes a transfer function whose output signal is directly proportional to the input.

- __linear PCM__

  Short for_linear pulse code modulation_ A linear and lossless uncompressed audio data format.  _PCM_ is usually assumed to mean _linear PCM_, but sometimes the adjective _linear_ is used to differentiate from nonlinear PCM formats. See also [pulse-code modulation (PCM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdeuskg).

- __loop__

  An excerpt of a recording, often a few seconds long or shorter, intended to be played repeatedly as part of a larger composition.

- __lossless compression__

  Data size reduction without loss of information. Common lossless audio compression formats include FLAC (free lossless audio codec) and [Apple Lossless](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceineucsch). Compare [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkinaukq2b).

- __lossy compression__

  Data size reduction that entails loss of information. Common lossy audio compression formats include [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijbeiqsi), [AAC (Advanced Audio Coding)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbcugrck), and [IMA ADPCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizcugrch). See also [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi). Compare [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizduqssb).

- __loudness__

  A subjective term to describe perceived sound intensity. When [SPL (sound pressure level)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvgy) increases by 10, loudness approximately doubles. Compare [gain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzy), [volume](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvhe).

- __LPCM__

  See [linear PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbduqrsk).

- __magic cookie__

  Also called _cookie_. In digital audio, an opaque data structure for transporting audio format metadata. For audio formats that use them, such as AAC, a magic cookie is produced during encoding, accompanies the data stream that it describes, and is employed during decoding. Magic cookie data is not accessed directly, but rather via a codec-specific interface.

- __MIDI (Musical Instrument Digital Interface)__

  A standard data protocol for communication between computers and electronic music instruments, first adopted in 1983 by the [AES (Audio Engineering Society)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztge). Core Audio uses MIDI to communicate with [instrument unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgy) audio units. MIDI data describes musical events, such as the starting or stopping of a note. Pronounced “MID-ee.”

- __MIDI endpoint__

  An abstract representation of a MIDI cable connection (or [port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzt)) as used by Core MIDI.

- __MIDI entity__

  In Core MIDI, a logical grouping of MIDI endpoints. For example, a MIDI driver may group a MIDI-in and a MIDI-out endpoint together in a MIDI entity. See also [MIDI endpoint](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgq).

- __MIDI port__

  A one-way (send or receive) connection point in a hardware-based or virtual MIDI network. Each port can support up to 16 channels of MIDI data. In Core MIDI, a port is represented abstractly in software by a MIDI endpoint. See also [MIDI (Musical Instrument Digital Interface)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkjbbukssb).

- __MIDI timecode (MTC)__

  A music synchronization protocol, defined as part of the [MIDI (Musical Instrument Digital Interface)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkjbbukssb) protocol. MIDI timecode emulates [SMPTE timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceinbeqqkb). See also [timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijfemq2j).

- __mLAN (music local area network)__

  A [FireWire](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceireumscf)-based interconnection protocol that carries multichannel audio and MIDI over a single cable. See also [MIDI (Musical Instrument Digital Interface)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkjbbukssb).

- __monophonic__

  Describes an instrument that plays only one note at a time. Compare [polyphonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyge). See also [monotimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygi), [multitimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygm).

- __monotimbral__

  In Core Audio, describes an [instrument unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgy) configured to produce sounds of only a single timbre. Both [monophonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyga) and [polyphonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyge) instrument units can be monotimbral. Compare [multitimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygm).

- __MP3__

  Common short form for _MPEG-1, audio layer 3_. A lossy, perceptual compression format for audio data that can achieve 10:1 data compression with usable sound quality. MPEG-1 does not define a standard encoding algorithm for MP3; it specifies only the decoding algorithm, the bit stream (packet) format, and the file format. See also [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi).

- __MP4__

  The [MPEG-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgu) audio/video container format, also known as MPEG-4 Part 14. MP4 files can hold many different types of data, such as AAC and MP3 audio, or MPEG-2 and H.264 video. Typically, files with the `.mp4` extension contain both audio and video data, while `.m4a` denotes files containing only audio data.

- __MPEG (Moving Picture Experts Group)__

  An international working group of ISO/IEC that develops standards for digitally-coded representations of audio and video. MPEG is part of the names of many [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi) formats published by the group. Pronounced “EM-peg.” See also [IEC (International Electrotechnical Commission)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbegrcj), [ISO (International Organization for Standardization)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizeeer2d).

- __MPEG-1__

  A set of audio and video [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuha) formats, formally designated as ISO/IEC-11172. MPEG-1 encompasses the Video CD and [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuhe) formats.

- __MPEG-1, audio layer 3__

  See [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijbeiqsi).

- __MPEG-2__

  A set of audio and video [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuha) formats, formally designated as ISO/IEC-13818, first published in 1994. MPEG-2 encompasses formats of generally higher quality than MPEG-1, including broadcast-quality video and (with modifications) DVD movies.

- __MPEG-2 AAC__

  See [AAC (Advanced Audio Coding)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbcugrck).

- __MPEG-4__

  A set of audio and video [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuha) formats, formally designated as ISO/IEC-14496, first published in 1998. MPEG-4 encompasses many of the features introduced in MPEG-1 and MPEG-2 and adds features useful for streaming media and broadcast, among others.

- __MPEG-4 AAC__

  See [AAC (Advanced Audio Coding)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbcugrck).

- __MPEG-4 Part 14__

  See [MP4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgq).

- __MTC__

  See [MIDI timecode (MTC)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceiveeeqki).

- __multiplexing__

  A synonym for [interleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjcuirse).

- __multitimbral__

  In Core Audio, describes an [instrument unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgy) configured to allow production of more than one timbre simultaneously. Compare [monotimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygi).

- __music player__

  The Core Audio programming construct that applications use to play MIDI or other event data.

- __mutex (mutual exclusion)__

  An algorithm or object used to avoid concurrent use of unsharable resources in a multithreaded environment.

- __node__

  An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) in an [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzu). Each node has one or more inputs and outputs that must be connected to other audio units. See also [head node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgy).

- __noise__

  Undesired energy or data components in a communication channel included with the signal that the channel is carrying. See also [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijdeqssc), [quantization noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjcucssi). Compare [distortion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5cuiskc).

- __noise floor__

  The amplitude of the [noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbbuissj) in a communication channel when no signal is present, typically measured as a scalar, absolute level in decibels relative to a standard level such as using [dBu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivbuisck). Noise can vary according to frequency, and perceived noise is subject to psychoacoustics, so the derivation of a single number to describe noise floor can entail weighting. Common weighting schemes are dBA, dBC, and unweighted.

- __Nyquist frequency__

  The highest frequency signal that can be faithfully recorded for a given sampling rate. Attempts to sample a signal containing higher frequencies results in the generation of an alias signal below the Nyquist frequency. The Nyquist frequency is half the sampling rate. See also [aliasing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsga).

- __Ogg__

  A free collection of digital codecs for multimedia, including [Ogg Vorbis](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygy) for lossy compression of audio at medium-to-high bit rates, and [Ogg FLAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygu) for lossless audio.

- __Ogg FLAC__

  A free, open source, lossless audio codec. Ogg FLAC typically compresses CD audio by 50% with no data loss. FLAC is an acronym for Free Lossless Audio Codec. See also [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizduqssb).

- __Ogg Vorbis__

  A free, open source, lossy audio codec intended to compete with [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijbeiqsi).

- __output audio queue__

  Also called _playback audio queue_. See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgu).

- __output unit__

  An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) of type `'auou'`. Output units can start and stop the flow of audio data in the signal chain. Examples include the [default output unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzge) and the [AUHAL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvgq). See also [head node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgy).

- __packet__

  In Core Audio, an encoding-defined unit of audio data comprising one or more frames. For PCM audio, each packet corresponds to one frame. For compressed audio, each packet corresponds to an encoding-defined number of uncompressed frames. For example, one packet of MPEG-2 AAC data decompresses to 1,024 frames of PCM data. In information technology, a packet is a block of data formatted for delivery over a network. Compare [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgi), [sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdecrsh).

- __packet description__

  In a variable-packet-size audio file or stream, metadata that specifies where a packet of audio data starts as well as its size. In Core Audio, a data structure used to represent a packet description in an audio data buffer. See also [packet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfduuscc), [packet table](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgy).

- __packet table__

  In a variable-packet-size audio file or stream, metadata consisting of a table of packet descriptions. See also [packet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfduuscc), [packet description](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwg4).

- __panner unit__

  In Core Audio, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) of type `'aupn'` that distributes a set of input channels, using a [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgq) algorithm, to a set of output channels. In the simplest case, a panner unit places a monaural signal at a left/right spot in a stereo field.

- __panning__

  From “panorama.“ In audio, the placement of a monaural signal within a stereo or multichannel (such as [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxg4)) sound field. Variations include stereo, [SoundField](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgi), spherical head, vector, and [HRTF (head related transfer function)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgy) panning. A more general term for panning is [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgq).

- __parameter__

  In an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceincumq2k), a variable that defines an adjustable attribute such as volume, pitch, or filter cutoff frequency. Each audio unit parameter has a name, a unit (such as Hertz or decibels), a default value and a value range, and an optional set of flags. In an [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgu), a parameter has only a value. Compare [element](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkjjcugscb), [property](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5beir2h), [scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsscirausr2k).

- __parser__

  In Audio File Stream Services, a software object of type `AudioFileStreamID`, used for reading audio file streams. In computer science generally, a program that works with a tokenizer to interpret a sequence of tokens.

- __perceptual coding__

  Lossy compression that takes advantage of limitations in human perception. In perceptual coding, audio data is selectively removed based on how unlikely it is that a listener will notice the removal. MP3 and MPEG-2 AAC are popular examples of perceptual coding. See also [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkinaukq2b).

- __PCM__

  See [pulse-code modulation (PCM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdeuskg).

- __pitch__

  In [psychoacoustics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgm), a perceptual sound attribute that is roughly correlated with frequency. In general, pitch increases as the perceptually-dominant sound frequency increases. The strength of a pitch sensation depends on the sound character; noise-like sounds cause a weak pitch sensation, while pure tones evoke a strong pitch sensation.

- __playback audio queue__

  Also called _output audio queue_. See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgu).

- __player__

  See [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivduiqsd).

- __plug-in__

  A portable collection of code that software applications can load and access through a standardized interface. For example, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) is a plug-in whose interface is defined by the OS X Component Manager.

- __polyphonic__

  Describes an instrument capable of playing more than one note simultaneously. Compare [monophonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyga). See also [monotimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygi), [multitimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygm).

- __port__

  See [MIDI port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvgm).

- __preset__

  In Core Audio, a property whose value is a predefined set of [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5aukr2j) values for an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceincumq2k).

- __priming__

  Adding [leading frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha4q) or [trailing frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrheya) to a set of audio data to support format conversion or [sample rate conversion (SRC)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha3q). If a converter requires priming and no leading or trailing frames are available, silent priming frames are typically used. See also [priming frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzugi).

- __priming frame__

  A [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgi) of audio data used for [priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuge).

- __property__

  In Core Audio, a key-value pair that declares an attribute or behavior, such as audio data stream format or latency. Each property has an associated data type to hold its value. Properties are typically non-time-varying and not directly settable by the user. Compare [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5aukr2j).

- __psychoacoustics__

  The study of the perception of sound. The development of [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivcugrsi) techniques relies on psychoacoustics.

- __pulse-code modulation (PCM)__

  A lossless encoding technique widely used for working with audio, invented by Alec H. Reeves in 1937. Sometimes called _LPCM_ for _linear pulse-code modulation_, which distinguishes the process from [ADPCM (adaptive delta pulse code modulation)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxhe). In pulse-code modulation, an analog signal is linearly encoded to a series of binary numbers by sampling an analog signal at regular intervals. See also [encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijduescb), [linear](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizbeossi), [quantization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbegssk).

- __pull__

  In Core Audio, to request and receive audio data, typically from a [buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbbemscc). Data typically moves through an [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzu) by way of a cascade of pull requests initiated by the [head node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijbuqr2k). The head node pulls, and each object upstream passes on the pull until the cascade reaches an audio data source.

- __quantization__

  The process of representing an analog (continuous-scale) value by a digital (discrete-scale) value. Quantization is characterized by a [bit depth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceinbeosce), which determines the dynamic range that can be represented, and a scaling factor, which determines the ratio between the analog and digital scales.

- __quantization error__

  The difference between an original analog signal value and its quantized digital representation. Quantization can sometimes results in a signal-correlated noise called [quantization noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrhe). See also [dither](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgy).

- __quantization noise__

  Signal-correlated [noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbbuissj) resulting from rounding errors when quantizing a series of data samples. Application of a [dither](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgy) signal during analog-to-digital conversion can decorrelate quantization noise from the signal. The perceptual result is low-amplitude noise instead of distortion.

- __recording audio queue__

  Also called _input audio queue_. See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgu).

- __reference distance__

  In Core Audio, for a [panner unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzygq), a [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5aukr2j) that specifies the real or apparent distance of an audio source from the listener beyond which the source’s level attenuates.

- __render__

  In Core Audio, to apply a recipe or specification for signal processing to some audio data. An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) typically contains a rendering method to obtain audio data and perform processing.

- __resampling__

  The process of taking samples of a digitized signal at a rate different from that of the original recording. Specific types of resampling include downsampling (resampling at a rate lower than the original) and upsampling (resampling at a higher rate).

- __reset__

  1. For audio units, to return an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceincumq2k) to its just-initialized state. 2. For codecs, to clear the codec’s input [buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbbemscc) and return the codec to its just-initialized state.

- __reverb__

  See [reverberation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceincecrce).

- __reverberation__

  An acoustic phenomenon produced by the cumulative addition of multiple sound reflections. Apple supplies the matrix reverb audio unit to simulate reverberation using [digital signal processing (DSP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjbuesce).

- __reverse multiplexing__

  A synonym for [deinterleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijceer2g).

- __RIFF (Resource Interchange File Format)__

  A minor variation on [IFF (Interchange File Format)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizdeersd) that uses little-endian integers.

- __RMS (root mean square)__

  A statistical measure of a time-varying value, such as voltage, current, or sound pressure. An RMS value is derived as the square root of the mean of the squares of a series of values. In the case of a continuously varying value, it is derived from an integration of the transfer function. For the special case of a sine wave signal, the calculation simplifies to Vrms = 0.707 \* Vpeak. May also be written in lowercase as _rms_.

- __safety offset__

  A property of an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) or other audio device that specifies a time lag, in samples, to allow for improved robustness of driver operation. The safety offset required for a given architecture includes time needed for memory access and to account for inaccuracies in a driver’s timestamp resolution. Safety offset contributes to [latency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejffesr2f).

- __sample__

  1. (noun) An instantaneous amplitude of the signal in a single audio channel, represented as an integer, floating-point, or fixed-point number. 2. (verb) To collect samples from an audio source, typically an analog audio source. Sampling typically involves collecting samples at regular, very brief intervals such as 1/44,100 seconds. 3. (noun) An excerpt of a longer recording. When the excerpt is intended to be played repeatedly, it is called a [loop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjfeiq2g). 4. (verb) To record a sample to use as a loop or for inclusion in a another recording. See also [fixed-point sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzg4).

- __sampling frequency__

  An alternate name for [sample rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivbukrch).

- __sample period__

  The time span from one sample to the next. The inverse of [sample rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivbukrch).

- __sample rate__

  During playback, the number of samples played per second for each channel of an audio file. During recording, the number of samples acquired per second for each channel. Also called _sampling rate_. More properly, but less commonly, called _sampling frequency_. Compare [frame rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjeugrcg).

- __sample rate conversion (SRC)__

  In digital audio, the process of converting PCM data from one sample rate to another.

- __SBR (Spectral Bandwidth Replication)__

  A technique used in [AAC (Advanced Audio Coding)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbcugrck) encoding (among other encoding technologies) to improve perceived audio quality.

- __scope__

  In Core Audio, a programmatic context within an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi). Unlike the general computer science notion of scopes, however, audio unit scopes cannot be nested. Each scope is a discrete context. You use scopes when writing code that sets or retrieves values of parameters or properties. Compare [element](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkjjcugscb). See also [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5aukr2j), [property](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5beir2h).

- __seek__

  To set an audio file or buffer’s read position to a specified [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgi).

- __sequence__

  In Core Audio, a collection of tracks to be played by a [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzz). A sequence always contains one or more event tracks and a tempo track. See also [event track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgu).

- __sequencer__

  Software or hardware for recording, playback, and editing of MIDI data or audio samples (excerpts or loops). See also [loop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejjfeiq2g),[MIDI (Musical Instrument Digital Interface)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawueqkkjbbukssb).

- __signal-to-noise ratio (SNR)__

  The range, expressed in decibels, between a nominal signal [level](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivdeoq2d) and the [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceijdeqssc). Compare [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceizaueqkd).

- __slice__

  The number of frames requested and processed during one rendering cycle of an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi). See also [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgi).

- __SMPTE (Society of Motion Picture and Television Engineers)__

  A US association of media professionals that publishes standards related to film, television, and audio. Pronounced “SIMP-tea.”

- __SMPTE timecode__

  A standard, time-based format for tagging film, video, and audio recordings to support [synchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbeegrsi) and editing. The SMPTE timecode represents a given time in the format `hours:minutes:seconds:frames`.

- __sonogram__

  Also called _spectrogram_. A three-dimensional visualization of a signal’s frequency content. Typically, a sonogram’s horizontal axis is time, its vertical axis is frequency, and the visual intensity (in terms of color or dot size) of each plotted point represents energy.

- __SoundField__

  A four-channel acoustic recording technique developed by British company SoundField, Ltd.

- __sound field__

  In acoustics, the space in which a sound is produced, conveyed to a listener, and perceived. In audio reproduction, the virtual space from which a monaural sound can seem to emanate. See also [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgq).

- __spatialization__

  The manipulation of audio signals to create perceived localization of sounds within a sound field. Compare [panning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwga). See also [sound field](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwhe).

- __spectrogram__

  See [sonogram](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgu).

- __S/PDIF (Sony/Phillips Digital Interface)__

  A consumer version of, and the inspiration for, the [AES-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceircemskc) format. Part of the IEC-60958 standard. Devices such as CD players and DAT recorders use S/PDIF.

- __SPL (sound pressure level)__

  A measure of sound intensity. SPL is commonly expressed as a ratio in decibels relative to 0 dB SPL, or as an absolute level in Pascals (Pa). While SPL is sometimes used to approximately indicate [loudness](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvg4), the correlation of SPL to loudness is complex due to perceptual factors. See also [weighting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzugq).

- __SRC__

  See [sample rate conversion (SRC)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha3q).

- __stream__

  1. (noun) A continuous flow of data over a [transmission channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgu) that can be interpreted as it is received. The packet boundaries used for encoding in a particular audio format may not coincide with transmission packet boundaries. 2. (verb) To send data as a stream. See also [audio file stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxga), [parser](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgi), [TCP (Transmission Control Protocol) stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgm).

- __surround sound__

  A loudspeaker configuration with more than two loudspeakers, intended to provide an [immersive audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzyha) experience. See also [5.1 Surround Sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwha).

- __sync__

  Common short form of _synchronize_. See [synchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbeegrsi).

- __synchronization__

  The process of ensuring that the clocks of two or more systems remain locked together, counting at the same rate. This term is commonly used in the context of locking an audio track to a video track. See also [clock](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejfduqski), [clock drift](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceincekqke), [SMPTE timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceinbeqqkb).

- __synchronous__

  In Audio Queue Services, describes one of two ways to stop an audio queue. Synchronous stopping happens immediately, without regard for previously buffered audio data. In digital communications, a transmission method that requires the clock frequency of the sender and receiver to be the same. Compare [asynchronous](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzwgi).

- __system output__

  In OS X, the hardware destination for all system sounds.

- __system output unit__

  An Apple-supplied [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) that connects with whichever hardware device the user has designated to be the [system output](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzv).

- __tail time__

  The time, beyond an audio unit’s latency, for a nominal-level signal to decay to silence at an audio unit’s output after it has gone instantaneously to silence at the input. Tail time is significant for audio units performing an effect such as delay or reverberation. An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) declares its tail time as a [property](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscei5beir2h).

- __TCP (Transmission Control Protocol) stream__

  A data stream used for audio delivery over networks. TCP is part of the IP (Internet Protocol) suite. It provides reliability and in-order delivery of packets, both of which are useful for audio data transmission. See also [audio file stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxga).

- __TDM (time division multiplexing)__

  A method of combining multiple digital signals in a single data stream by [interleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsg4) samples of each signal in time. For example, to carry a stereo signal on a single stream, the stream contains alternating samples of the left and right channels: L R L R L R.

- __tempo__

  The general speed of a piece of music, often described in beats per minute (BPM).

- __tempo track__

  A special track used to synchronize all the other tracks in a [sequence](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrge). See also [event track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgu).

- __threshold__

  A preset signal level at which some sort of processing is activated. For example, a compressor [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) can allow you to specify the threshold above which compression begins.

- __timbre__

  The perceived quality of a sound as distinct from pitch. volume, envelope, and duration. For example, a tuning fork can be described as having a “gentle” timbre, while a strongly hit crash cymbal can be described as having a “harsh” timbre.

- __timecode__

  A standardized indexing system for identifying specific portions of a audio file. Timecodes are often used for synchronizing or editing audio data. See also [SMPTE timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceinbeqqkb).

- __timeline__

  A visual representation of an audio signal over time.

- __TosLink__

  An optical cable standard used to transmit digital audio signals. Short for _ToshibaLink_.

- __track__

  See [event track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztgu). Compare [channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzthe).

- __trailing frames__

  In audio data format conversion, frames of audio data that follow, in time, the nominal ending frame for an input [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgq). See also [priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuge). Compare [leading frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrha4q).

- __transmission channel__

  A hardware or software conduit for the conveyance of a data [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgq) or an analog signal.

- __trim frames__

  Frames added to the beginning or end of a [buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbbemscc) to pad the audio data. Trim frames added before the audio data are typically used to prime an audio decompressor. See also [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzsgi),[priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzuge), [priming frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzugi).

- __uninitialize__

  To return an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) to its unconfigured state. Compare [reset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrg4).

- __unity gain__

  A [gain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzy) of 0 dB.

- __Universal Serial Bus (USB)__

  A serial bus standard for connecting hardware devices, such as computers, keyboards, and audio devices. Variations include USB 0.9, USB 1.0, USB 1.1, and USB 2.0. Specified by the USB Implementers Forum (USB-IF), an international industry standards body.

- __USB__

  See [Universal Serial Bus (USB)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvgi).

- __variable bit rate (VBR)__

  An encoding method available for some compression formats, such as AAC, that allows bit rate to vary according to the source material. The aim is to provide consistent perceived audio quality while minimizing file size. It does this by increasing the bit rate for difficult-to-encode portions and decreasing the bit rate for easy-to-encode portions. Compare [average bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzugy), [constant bit rate (CBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztha).

- __VBR__

  See [variable bit rate (VBR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgm).

- __virtual destination__

  In Core Audio, a designation by a software MIDI device indicating that it can receive MIDI data. Compare [virtual source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzx).

- __virtual source__

  A designation by a software MIDI device indicating that it can transmit MIDI data. Compare [virtual destination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzw).

- __V1__

  In Core Audio, the original version of the [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzrgi) interface, deprecated in OS X v10.2 and unsupported starting in OS X v10.5. V1 audio units differ from V2 audio units in that they supported [fan out](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgy), supported interleaved streams, and used a component type and subtype approach different from that of V2. New development should be done with the V2 audio unit interface. Compare [V2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgq).

- __V2__

  In Core Audio, the current version of the audio unit interface, recommended since OS X v10.2 and the only supported version starting with OS X v10.5. Compare [V1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzxgm).

- __volume__

  In [psychoacoustics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzzgm), the average perceived loudness of a sound. Compare [level](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceivdeoq2d).

- __WAV__

  A chunk-based digital audio file format originally developed for IBM-compatible PCs. While WAV files can hold compressed audio data, they most commonly hold uncompressed [linear PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugscejbduqrsk) data. WAV is a variant of the RIFF bitstream format. See also [RIFF (Resource Interchange File Format)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvztg4).

- __waveform__

  The shape of a signal when visualized as a graph showing its variation in amplitude over time.

- __wavelength__

  The span of one complete cycle in a repeating [waveform](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawugsceineugr2k).

- __weighting__

  Systematic adjustment of a measurement to highlight a particular criterion. For example, [SPL (sound pressure level)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinjtfvbuqmrrgawvgvzvgy) measurements can be weighted to approximate how people perceive sound, placing more emphasis on midrange frequencies than on higher or lower ones.

[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

