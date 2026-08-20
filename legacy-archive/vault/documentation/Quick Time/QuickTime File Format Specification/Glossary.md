---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFGloss/QTFFGloss.html
archived_at: '2026-07-27T06:57:06.901436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __AAC__

  Advanced Audio Coding (AAC) is a standardized, lossy compression and encoding scheme for digital audio. AAC generally achieves better sound quality than MP3 encoding at similar bit rates.

- __alpha channel__

  The upper bits of a display pixel, which control the blending of video and graphical image data for a video digitizer component.

- __alternate group__

  A set of related movie tracks (alternate tracks) that contain the same alternate group identifier in the track header.

- __alternate track__

  A movie track that contains alternate data for another track. QuickTime chooses one track from an alternate group to be used when the movie is played. The choice may be based on such considerations as image quality or localization. See also [track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugssciveeeqke).

- __API (Application Programming Interface)__

  The set of function calls, data structures, and other programming elements by which a structure of code (such as a system-level toolbox) can be accesses by other code (such as an application program).

- __atom__

  The basic unit of data in a movie resource, sprite, or other QuickTime data structure. There are a number of different atom types. There are two varieties of atoms: QT atoms, which may contain other atoms, and classic atoms, which do not contain any other atoms. See also [movie resource](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscijcusrkc), [sprite](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjbucr2d) , [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirauirsg), and [classic atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivcuqr2b).

- __atom container__

  A tree-structured hierarchy of QT atoms. See also [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirauirsg).

- __atom ID__

  A 32-bit integer that uniquely identifies an atom among other child atoms of the same parent atom. The root atom has an atom ID value of 0x0001. See also [child atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizdeussb), [parent atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirdugq2b) , and [root atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscineegqke).

- __atom type__

  A 32-bit value that uniquely identifies the data type of an atom. It is normally an `OSType`, rendered by four ASCII characters. An atom’s data type helps determine how the atom’s contents are interpreted.

- __audio track__

  An alternative name for the sound track for a QuickTime file. See [sound track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwvgvzrgezq).

- __background color__

  The color of the background behind a sprite or other image.

- __bit depth__

  The number of bits used to encode the color of each pixel in a graphics buffer.

- __chapter list__

  A set of named entry points into a movie, presented to the viewer as a text list.

- __child atom__

  A QT atom inside a container atom, which is its parent atom. See also [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirauirsg), [container atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjdeqqsf) , and [parent atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirdugq2b).

- __chunk__

  A collection of sample data in a media. Chunks, which may contain one or more samples, allow optimized data access. Chunks in a media may have different sizes, and the samples within a chunk may have different sizes.

- __classic atom__

  A QuickTime atom that contains no other atoms. A classic atom, however, may contain a table. An example of a classic atom is an edit list atom, containing the edit list table. Compare [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirauirsg).

- __clipped movie boundary region__

  The region that combines the union of all track movie boundary regions for a movie, which is the movie’s movie boundary region, with the movie’s movie clipping region, which defines the portion of the movie boundary region that is to be used. See also [movie boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivfesqsd) and [movie clipping region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjffesqse).

- __clipping__

  The process of defining the boundaries of a graphics area.

- __closed caption track__

  The closed caption text for a QuickTime movie, which is typically a direct transcription of a sound track and which is stored in a track with a media handler type of `'clcp'`.

- __container atom__

  An atom that contains other atoms, possibly including other container atoms.

- __creator signature__

  In the Macintosh file system, a four-character code that identifies the application program to which a file belongs.

- __data fork__

  In a legacy two-fork Macintosh file, the section that corresponds to a DOS/Windows file.

- __data handler__

  A piece of software that is responsible for reading and writing a media’s data. The data handler provides data input and output services to the media’s media handler. See also [media handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbfeurkg).

- __data reference__

  A reference to a media’s data.

- __decoder delay__

  The number of “pre-roll” audio samples needed to reproduce the source audio signal in an encoded audio stream for a given time index. See also [encoder delay](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwvgvzrgq).

- __display coordinate system__

  The QuickDraw graphics world, which can be used to display QuickTime movies, as opposed to the movie’s time coordinate system, which defines the basic time unit for each of the movie’s tracks. Compare [time coordinate system](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbcegq2j).

- __dithering__

  A technique used to improve picture quality when you are attempting to display an image that exists at a higher bit-depth representation on a lower bit-depth device. For example, you might want to dither a 24 bits per pixel image for display on an 8-bit screen.

- __dropframe__

  A synchronizing technique that skips time codes to keep them current with video frames.

- __duration__

  A time interval. Durations are time values that are interpreted as spans of time, rather than as points in time.

- __edit list__

  A data structure that arranges a media into a time sequence.

- __edit state__

  Information defining the current state of a movie or track with respect to an edit session. QuickTime uses edit states to support undo facilities.

- __effect description__

  A data structure that specifies which component will be used to implement an effect in a movie, and how the component will be configured.

- __effect track__

  A modifier track that applies an effect (such as a wipe or dissolve) to a movie. See [modifier track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizeecrcg).

- __encoder delay__

  The term used to describe the delay incurred during encoding to produce properly formed, encoded audio packets. See also [decoder delay](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwvgvzsgi) and [Background – AAC Encoding](Audio%20Priming%20-%20Handling%20Encoder%20Delay%20in%20AAC.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrnknlte).

- __file fork__

  A section of a Macintosh file. See also [data fork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjbemrsb), [resource fork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizbuiq2k).

- __file preview__

  A thumbnail picture from a movie that is displayed in the Open File dialog box. See also [thumbnail picture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizcumqkk).

- __fixed point__

  A point that uses fixed-point numbers to represent its coordinates. QuickTime uses fixed points to provide greater display precision for graphical and image data.

- __fixed rectangle__

  A rectangle that uses fixed points to represent its vertices. QuickTime uses fixed rectangles to provide greater display precision.

- __Flash__

  A vector-based graphics and animation technology. Flash data is exported as SWF files.

- __flattening__

  The process of copying all of the original data referred to by reference in QuickTime tracks into a QuickTime movie file. This can also be called resolving references. Flattening is used to bring in all of the data that may be referred to from multiple files after QuickTime editing is complete. It makes a QuickTime movie stand-alone—that is, it can be played on any system without requiring any additional QuickTime movie files or tracks, even if the original file referenced hundreds of files. The flattening operation is essential if QuickTime movies are to be used with CD-ROM discs.

- __frame__

  A single image in a sequence of images.

  For uncompressed audio, one sample from each channel. For compressed audio, a compressed group of samples whose format is dependent on the compressor.

- __frame rate__

  The rate at which a movie is displayed—that is, the number of frames per second that are actually being displayed. In QuickTime the frame rate at which a movie was recorded may be different from the frame rate at which it is displayed. On very fast machines, the playback frame rate may be faster than the record frame rate; on slow machines, the playback frame rate may be slower than the record frame rate. Frame rates may be fractional.

- __free atom__

  An atom of type '`free`', which you can include in a QuickTime file as a placeholder for unused space.

- __file type atom__

  An atom of type '`ftyp`', which defines which file specifications a file is compatible with.

- __graphics mode__

  The method by which two overlapping images are blended together to produce a composite image.

- __graphics world__

  A software environment in which a movie track or set of images may be defined before importing them into a movie.

- __handler reference atom__

  A QT atom of type 'hdlr' that specifies the media handler to be used to interpret a media. See also [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirauirsg), [media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugssci5eucqki), [media handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbfeurkg).

- __hint track__

  A track in a streaming movie that contains information for a packetizer about the data units to stream. See also [streaming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirceqqsi).

- __hot spot__

  An area, typically in a VR presentation, that the user can click to invoke an action.

- __hypertext__

  Action media that contains a URL and takes the user to a website.

- __identity matrix__

  A transformation matrix that specifies no change in the coordinates of the source image. The resulting image corresponds exactly to the source image. See also [transformation matrix](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbeuir2h).

- __image__

  In sprite programming, one of a sprite’s properties. See also [sprite](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjbucr2d), [PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbbemqsj).

- __image sequence__

  A series of visual representations usually represented by video over time. Image sequences may also be generated synthetically, such as from an animation sequence.

- __image track__

  Any track in a QuickTime movie that contains visual images. The term particularly applies to video tracks that contain VR data.

- __input map__

  A data structure that describes where to find information about tracks that are targets of a modifier track. See [modifier track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizeecrcg).

- __interlacing__

  A video mode that updates half the scan lines on one pass and goes through the second half during the next pass.

- __interleaving__

  A technique in which sound and video data are alternated in small pieces, so the data can be read off disk as it is needed. Interleaving allows for movies of almost any length with little delay on startup.

- __ISO__

  Acronym for the International Standards Organization. ISO establishes standards for multimedia data formatting and transmission, such as JPEG and MPEG.

- __Joint Photographic Experts Group (JPEG)__

  Refers to an international standard for compressing still images. This standard supplies the algorithm for image compression. The version of JPEG supplied with QuickTime complies with the baseline ISO standard bitstream, version 9R9. This algorithm is best suited for use with natural images.

- __key frame__

  A sample in a sequence of temporally compressed samples that does not rely on other samples in the sequence for any of its information. Key frames are placed into temporally compressed sequences at a frequency that is determined by the key frame rate. Typically, the term key frame is used with respect to temporally compressed sequences of image data. See also sync sample. See also [key frame rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugssciveuiscc).

- __key frame rate__

  The frequency with which key frames are placed into temporally compressed data sequences. See also [key frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizceor2i).

- __layer__

  A mechanism for prioritizing the tracks in a movie or the overlapping of sprites. When it plays a movie, QuickTime displays the movie’s tracks according to their layer—tracks with lower layer numbers are displayed first; tracks with higher layer numbers are displayed over those tracks.

- __leaf atom__

  An atom that contains only data, and no other atoms.

- __LPCM__

  Linear pulse-code modulation (LPCM) is a method of encoding audio information digitally. The term also refers collectively to formats using this method of encoding. The term pulse-code modulation (PCM), though strictly more general, is often used to describe data encoded as LPCM. LPCM is PCM with linear quantization. See also [PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbbemqsj).

- __matrix__

  See [transformation matrix](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbeuir2h).

- __matte__

  A defined region of a movie display that can be clipped and filled with another display.

- __media__

  A data structure that contains information that describes the data for a track in a movie. Note that a media does not contain its data; rather, a media contains a reference to its data, which may be stored on disk, CD-ROM disc, or any other mass storage device. Also called a _media structure_.

- __media handler__

  A piece of software that is responsible for mapping from the movie’s time coordinate system to the media’s time coordinate system. The media handler also interprets the media’s data. The data handler for the media is responsible for reading and writing the media’s data. See also [data handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizfesrcd).

- __MIDI__

  Acronym for Musical Instrument Digital Interface, a standard format for sending instructions to a musical synthesizer.

- __modifier track__

  A track in a movie that modifies the data or presentation of other tracks. For example, a tween track is a modifier track. See also [tween track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjduiqsj).

- __movie__

  A structure of time-based data that is managed by QuickTime. A movie may contain sound, video, animation, or a combination of any of these types of data. A QuickTime movie contains one or more tracks; each track represents a single data stream in the movie. See also [time-based data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirauisse), [track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugssciveeeqke).

- __movie boundary region__

  A region that describes the area occupied by a movie in the movie coordinate system, before the movie has been clipped by the movie clipping region. A movie’s boundary region is built up from the track movie boundary regions for each of the movie’s tracks. See also [movie clipping region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjffesqse), [track movie boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjeeessb).

- __movie clipping region__

  The clipping region of a movie in the movie’s coordinate system. QuickTime applies the movie’s clipping region to the movie boundary region to obtain a clipped movie boundary region. Only that portion of the movie that lies in the clipped movie boundary region is then transformed into an image in the display coordinate system. See also [movie boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivfesqsd).

- __movie display boundary region__

  A region that describes the display area occupied by a movie in the display coordinate system, before the movie has been clipped by the movie display clipping region. See also [movie display clipping region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjeeossb).

- __movie display clipping region__

  The clipping region of a movie in the display coordinate system. Only that portion of the movie that lies in the clipping region is visible to the user. QuickTime applies the movie’s display clipping region to the movie display boundary region to obtain the visible image. See also [movie display boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirdueq2j).

- __movie file__

  A QuickTime file that stores a movie and its associated data.

- __movie header atom__

  A QT atom that specifies the characteristics of an entire QuickTime movie.

- __movie poster__

  A single visual image representing a QuickTime movie. You specify a poster as a point in time in the movie and specify the tracks that are to be used to constitute the poster image.

- __movie preview__

  A short dynamic representation of a QuickTime movie. Movie previews typically last no more than 3 to 5 seconds, and they should give the user some idea of what the movie contains. You define a movie preview by specifying its start time, its duration, and its tracks.

- __movie resource__

  One of several data structures that provide the medium of exchange for movie data between applications on a Macintosh computer and between computers, even computers of different types.

- __movie sprite__

  A sprite that lives in a sprite track and acts in a movie. See also [sprite track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjbuurcd).

- __MPEG-4__

  An ISO standard (based on the QuickTime file format) that supports video and audio streaming. See also [streaming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscirceqqsi).

- __music__

  One of the QuickTime media types, in which sequences of sounds and tones are generated.

- __National Television System Committee (NTSC)__

  Refers to the color-encoding method adopted by the committee in 1953. This standard was the first monochrome-compatible, simultaneous color transmission system used for public broadcasting. This method is used widely in the United States.

- __node__

  Either a panorama or an object in a QuickTime VR movie.

- __NTSC__

  See National Television System Committee.

- __object track__

  A track in a QuickTime VR movie that contains a set of views of a VR object.

- __offset-binary encoding__

  A method of digitally encoding sound that represents the range of amplitude values as an unsigned number, with the midpoint of the range representing silence. For example, an 8-bit sound sample stored in offset-binary format would contain sample values ranging from 0 to 255, with a value of 128 specifying silence (no amplitude). Samples in Macintosh sound resources are stored in offset-binary form. Compare [twos-complement encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjfcuoscf).

- __PAL__

  See [Phase Alternation Line (PAL)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscinbeerkg).

- __packet__

  For uncompressed audio, a sample from a single channel. For compressed audio, this field has no real meaning; by convention, it is treated as 1/number-of-channels.

- __panorama__

  A structure of QuickTime VR data that forms a virtual-world environment within which the user can navigate.

- __panorama track__

  A track in a QuickTime VR movie that contains a panorama.

- __parent atom__

  A QT atom that contains other QT atoms, which are its child atoms. See also [child atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscizdeussb).

- __Phase Alternation Line (PAL)__

  A color-encoding system used widely in Europe, in which one of the subcarrier phases derived from the color burst is inverted in phase from one line to the next. This technique minimizes hue errors that may result during color video transmission. Sometimes called Phase Alternating Line.

- __playback quality__

  A relative measure of the fidelity of a track in a QuickTime movie. You can control the playback (or language) quality of a movie during movie playback. QuickTime chooses tracks from alternate tracks that most closely correspond to the display quality desired. See also [alternate track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscijaumrkk).

- __poster__

  A frame shot from a movie, used to represent its content to the user.

- __preferred rate__

  The default playback rate for a QuickTime movie.

- __preferred volume__

  The default sound volume for a QuickTime movie.

- __preview__

  A short, potentially dynamic, visual representation of the contents of a file. The Standard File Package can use previews in file dialog boxes to give the user a visual cue about a file’s contents. See also [file preview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivdugsce).

- __preview atom__

  An atom of type 'pnot', which can appear in a QuickTime file to contain a movie’s file preview.

- __profile atom__

  An atom of type 'prfl', which summarizes the features of a movie or track.

- __property__

  Information about a sprite that describes its location or appearance. One sprite property is its image, the original bitmapped graphic of the sprite.

- __PCM__

  Pulse-code modulation (PCM) is a method used to digitally represent sampled analog signals (typically audio related in QuickTime references). See also [LPCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwvgvzr).

- __QT
  atom__

  A QuickTime atom that contains other atoms, possibly including other QT atoms and classic atoms. A data reference atom is an example of a QT atom. Compare [classic atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivcuqr2b).

- __QTMA (QuickTime Music Architecture)__

  The part of QuickTime that lets other code create and manipulate music tracks in movies.

- __QTVR track__

  A track in a QuickTime movie that maintains a list of VR nodes.

- __QuickDraw__

  The original Mac OS two-dimensional drawing software, used by QuickTime.

- __QuickTime__

  A set of Macintosh system extensions or a Windows dynamic-link library that other code can use to create and manipulate time-based data.

- __QuickTime VR__

  A QuickTime media type that lets users interactively explore and examine photorealistic three-dimensional virtual worlds. QuickTime VR data structures are also called panoramas.

- __rate__

  A value that specifies the pace at which time passes for a time base. A time base’s rate is multiplied by the time scale to obtain the number of time units that pass per second. For example, consider a time base that operates in a time coordinate system that has a time scale of 60. If that time base has a rate of 1, 60 time units are processed per second. If the rate is set to 1/2, 30 time units pass per second. If the rate is 2, 120 time units pass per second. See also [time base](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjjcekq2k) and [time unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscijcusrsc).

- __resource__

  In Macintosh programming, an entity in a file or in memory that may contain executable code or a description of a user interface item. Resources are loaded as needed by a resource manager, and are identified by their type and ID number.

- __resource fork__

  In a legacy Macintosh file, the section that contains resources. The use of the resource fork for storage of QuickTime media is deprecated in the QuickTime file format.

- __root atom__

  The largest atom container in a hierarchy, with atom type 'sean'.

- __sample__

  A single element of a sequence of time-ordered data.

- __sample format__

  The format of data samples in a track, such as a sprite track.

- __sample number__

  A number that identifies the sample with data for a specified time.

- __SECAM (Systeme Electronique Couleur avec Memoire)__

  Sequential Color With Memory; refers to a color-encoding system in which the red and blue color-difference information is transmitted on alternate lines, requiring a one-line memory in order to decode green information.

- __skip atom__

  An atom of type 'skip', which you can include in a QuickTime file as a placeholder for unused space.

- __SMPTE__

  Acronym for Society of Motion Picture and Television Engineers, an organization that sets video and movie technical standards.

- __sound track__

  The audio for a QuickTime file, which is stored in a track with a media handler type of `'soun'`.

- __sprite__

  An animated image that is managed by QuickTime. A sprite is defined once and is then animated by commands that change its position or appearance.

- __sprite track__

  A movie track populated by movie sprites.

- __streaming__

  Delivery of video or audio data over a network in real time, to support applications such as videophone and video conferencing. See [MPEG-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivfekqsg).

- __string atom__

  An atom in VR media that contains text.

- __subtitle track__

  The subtitle text for a QuickTime movie, which is typically a translation from the language of the sound track into a different language and which is stored in a track with a media handler type of `'sbtl'`.

- __SWF files__

  Files that contain Flash data. See [Flash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivceorke).

- __sync sample__

  A sample that does not rely on preceding frames for content. See also key frame.

- __Systeme Electronique Couleur avec Memoire__

  See SECAM.

- __temporal compression__

  Image compression that is performed between frames in a sequence. This compression technique takes advantage of redundancy between adjacent frames in a sequence to reduce the amount of data that is required to accurately represent each frame in the sequence. Sequences that have been temporally compressed typically contain key frames at regular intervals.

- __text track__

  General-purpose text that displays in a QuickTime movie, which is represented as an atom of type 'text'.

- __thumbnail picture__

  A picture that can be created from an existing image that is stored as a pixel map, a picture, or a picture file. A thumbnail picture is useful for creating small representative images of a source image and in previews for files that contain image data.

- __time base__

  A set of values that define the time basis for an entity, such as a QuickTime movie. A time base consists of a time coordinate system (that is, a time scale and a duration) along with a rate value. The rate value specifies the speed with which time passes for the time base.

- __time-based data__

  Data that changes or interacts with the user along a time dimension. QuickTime is designed to handle time-based data.

- __timecode media__

  A media of type 'tmcd' that is used to store timecode data.

- __timecode track__

  A movie track that stores external timing information, such as SMPTE time codes.

- __time coordinate system__

  A set of values that defines the context for a time base. A time coordinate system consists of a time scale and a duration. Together, these values define the coordinate system in which a time value or a time base has meaning.

- __time scale__

  The number of time units that pass per second in a time coordinate system. A time coordinate system that measures time in sixtieths of a second, for example, has a time scale of 60.

- __time unit__

  The basic unit of measure for time in a time coordinate system. The value of the time unit for a time coordinate system is represented by the formula (1/time scale) seconds. A time coordinate system that has a time scale of 60 measures time in terms of sixtieths of a second.

- __time value__

  A value that specifies a number of time units in a time coordinate system. A time value may contain information about a point in time or about a duration.

- __track__

  A Movie Toolbox data structure that represents a single data stream in a QuickTime movie. A movie may contain one or more tracks. Each track is independent of other tracks in the movie and represents its own data stream. Each track has a corresponding media, which describes the data for the track.

- __track boundary region__

  A region that describes the area occupied by a track in the track’s coordinate system. QuickTime obtains this region by applying the track clipping region and the track matte to the visual image contained in the track rectangle.

- __track clipping region__

  The clipping region of a track in the track’s coordinate system. QuickTime applies the track’s clipping region and the track matte to the image contained in the track rectangle to obtain the track boundary region. Only that portion of the track that lies in the track boundary region is then transformed into an image in the movie coordinate system.

- __track header atom__

  A QT atom that specifies the characteristics of a track in a QuickTime movie.

- __track height__

  The height, in pixels, of the track rectangle.

- __track input map__

  A structure of QT atoms that specifies how secondary data for a track is to be interpreted (clipping, blending, etc.).

- __track load settings__

  Information that specifies how and when a track is to be preloaded before running in a movie.

- __track matte__

  A pixel map that defines the blending of track visual data. The value of each pixel in the pixel map governs the relative intensity of the track data for the corresponding pixel in the result image. QuickTime applies the track matte, along with the track clipping region, to the image contained in the track rectangle to obtain the track boundary region. See [track matte](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugssci5cuesse), [track rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjbeeosci), and [track boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscivcumssi).

- __track movie boundary region__

  A region that describes the area occupied by a track in the movie coordinate system, before the movie has been clipped by the movie clipping region. The movie boundary region is built up from the track movie boundary regions for each of the movie’s tracks.

- __track offset__

  The blank space that represents the intervening time between the beginning of a movie and the beginning of a track’s data. In an audio track, the blank space translates to silence; in a video track, the blank space generates no visual image. All of the tracks in a movie use the movie’s time coordinate system. That is, the movie’s time scale defines the basic time unit for each of the movie’s tracks. Each track begins at the beginning of the movie, but the track’s data might not begin until some time value other than 0.

- __track reference__

  A data structure that defines the relation between movie tracks, such as the relation between a timecode track and other tracks. See [timecode track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscjfeussse).

- __track rectangle__

  A rectangle that completely encloses the visual representation of a track in a QuickTime movie. The width of this rectangle in pixels is referred to as the track width; the height, as the track height.

- __track width__

  The width, in pixels, of the track rectangle.

- __transformation matrix__

  A 3-by-3 matrix that defines how to map points from one coordinate space into another coordinate space.

- __tween data__

  The data in a tween track, such as interpolation values.

- __tween track__

  A modifier track that performs a specific kind of tweening, such as path-to-matrix rotation.

- __tweening__

  A process interpolating new data between given values in conformance to an algorithm. It is an efficient way to expand or smooth a movie’s presentation between its actual frames.

- __twos-complement encoding__

  A system for digitally encoding sound that stores the amplitude values as a signed number—silence is represented by a sample with a value of 0. For example, with 8-bit sound samples, twos-complement values would range from –128 to 127, with 0 meaning silence. The Audio Interchange File Format (AIFF) stores samples in twos-complement form. Compare [offset-binary encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugssci5dukscb).

- __URL__

  The address of a website.

- __user data__

  Auxiliary data that your application can store in a QuickTime movie, track, or media structure. The user data is stored in a user data list; items in the list are referred to as user data items. Examples of user data include a copyright, date of creation, name of a movie’s director, and special hardware and software requirements. See also [user data list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscijbugscc), [user data item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgmwugsscircuosck)

- __user data item__

  A single element in a user data list, such as a modification date or copyright notice.

- __user data list__

  The collection of user data for a QuickTime movie, track, or media. Each element in the user data list is called a user data item.

- __VR (virtual reality)__

  See QuickTime VR.

- __Wired Sprite__

  A sprite such as a clickable button that has wired actions associated with it.

[Previous](Document%20Revision%20History.md)
