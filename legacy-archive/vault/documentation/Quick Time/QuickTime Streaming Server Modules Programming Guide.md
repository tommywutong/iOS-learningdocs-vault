---
title: QuickTime Streaming Server Modules Programming Guide
apple_id: TP30001143
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTSS/Preface/Preface.html
archived_at: '2026-07-18T02:05:03.799847Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/QTSS/Concepts/QTSSConcepts.html)

# About This Manual

|  |  |
| --- | --- |
| __Framework__ | None. |
| __Declared in__ | QTSS.h |

This manual describes version 5.0 of the programming
interface for creating QuickTime Streaming Server (QTSS) modules
for the open source Darwin Streaming Server. The QTSS programming
interface provides an easy way for developers to add new functionality
to the Streaming Server. This version of the programming interface
is compatible with QuickTime Streaming Server version 5.5.

This chapter describes the callback rotuines and data types
that modules use to call the QuickTime Streaming Server.

Version 5.0 of the QTSS programming interface provides the
following new features:

- These new internal server preferences have been
  added: `disable_thinning`, `player_requires_rtp_header_info`,
  and `player_requires_bandwidth_adjustment`.
- These new preferences have been added to the `QTSSFileModule` module
  for compatibility with 3rd Generation Partnership Project (3GPP)
  players: `compatibility_adjust_sdp_media_bandwidth_percent` and `enable_player_compatibility`.
- RTP play information is now enabled by default in the `QTSSReflectorModule` module. Use
  the new preference, `disable_rtp_play_info` to
  disable RTP Play information. Another new `QTSSReflectorModule` preference
  is `reflector_rtp_info_offset_msec`.
  For compatibility with 3GPP players, these preferences have also
  been added to the `QTSSReflectorModule` module: `enable_play_response_range_header`, `enable_player_compatibility`,
  and `force_rtp_info_sequence_and_time`.
- This new preference has been added to the `QTSSFlowControlModule` module: `flow_control_udp_thinning_module_enabled`.

The following changes have been made to existing preferences:

- Default size of the `QTSSFileModule` preference `shared_buffer_unit_k_size` has
  been increased from 32 to 64.
- Default size of the `QTSSFileModule` preference `private_buffer_unit_k_size` has
  been increased from 32 to 64.

The `enable_rtp_play_info` preference
has been removed from the `QTSSReflectorModule` module.

The `-D` command
line option has been added to the StreamingServer. When specified,
the `-D` option outputs
performance status information.

The file `streamingloadtool.conf`,
installed in `/Library/QuickTimeStreaming/Config`,
has new file tags:

- `player` _text_,
  where _text_ is the name of the RTSP player.
  The information is sent to the server as the UserAgent header.
- `sendoptions` _setting_,
  where _setting_ is `yes` or `no`.
  If `yes`, a Send Options
  request is made before the `DESCRIBE` statement.
- `requestrandomdata` _setting_,
  where _setting_ is `yes` or `no`.
  Set _setting_ to `yes` to
  ask for random data from the server.
- `randomdatasize` _setting_,
  where _setting_ is a number from 0 to 262144
  that specifies the number of random bytes the server should send.

The `Letter Gothic` font
is used to indicate text that you type or see displayed. This manual includes
special text elements to highlight important or supplemental information:

Go to [http://www.opensource.apple.com](http://www.opensource.apple.com/) to
register as a member of the Apple open source community. Then download
the source code for the Darwin Streaming Server at [http://www.publicsource.apple.com/projects/streaming](http://www.publicsource.apple.com/projects/streaming).
The source code’s Documentation directory contains valuable information:

- `AboutTheSource.html`
- `DevNotes.html`
- `SourceCodeFAQ.html`

The following RFCs provide additional information of interest
to developers of QuickTime Streaming Server modules and are available
at many locations on the Internet:

- RFC 2326, Real Time Streaming Protocol (RTSP)
- RFC 1889, RTP: A Transport Protocol for Real-Time Applications
- RFC 2327, SDP: Session Description Protocol
- RFC 2616, HTTP 1.1

For an overview of the Darwin Streaming Server and links to
the latest QuickTime information, go to [http://developer.apple.com/darwin/projects/streaming](https://developer.apple.com/darwin/projects/streaming).

Go to [http://developer.apple.com/documentation/quicktime](https://developer.apple.com/documentation/quicktime) for
QuickTime developer documentation.

Communicate with other Darwin Streaming Server developers
by joining the discussion list at [http://lists.apple.com/mailman/listinfo/streaming-server-dev](http://lists.apple.com/mailman/listinfo/streaming-server-dev).

See what with other Darwin Streaming Server developers are
doing by joining the discussion list at [http://lists.apple.com/mailman/listinfo/publicsource-modifications](http://lists.apple.com/mailman/listinfo/publicsource-modifications).

[Next](https://developer.apple.com/library/archive/documentation/QuickTime/QTSS/Concepts/QTSSConcepts.html)

