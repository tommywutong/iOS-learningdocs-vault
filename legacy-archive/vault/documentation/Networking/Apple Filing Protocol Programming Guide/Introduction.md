---
title: Apple Filing Protocol Programming Guide
apple_id: TP40000854
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:10.203601Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Apple%20Filing%20Protocol%20Concepts.md)

# Introduction

The Apple Filing Protocol (AFP) allows users of multiple computers to share files easily and efficiently over a network.

This document describes the AFP wire protocol at a conceptual level. For detailed information about the request blocks that an AFP client sends to an AFP server and the reply blocks that an AFP server sends to an AFP client in response to a request block, see _Apple Filing Protocol Reference_.

Note that all values exchanged between an AFP client and an AFP server are sent over the network in network byte order.

This book contains the following chapters:

- [Apple Filing Protocol Concepts](Apple%20Filing%20Protocol%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqmznknltc) describes the concepts used in the AFP architecture.
- [Using Login Commands](Using%20Login%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqnbnknltc) describes the commands used to open and close a connection with a file server.
- [Using Volume Commands](Using%20Volume%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqmrsgewvgvzr) describes the commands for interacting with a file server volume.
- [Using Directory Commands](Using%20Directory%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqmrsgiwvgvzr) describes the commands for using directories.
- [Using File Commands](Using%20File%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqmrsgmwvgvzr) describes the commands for working on files.
- [Using Combined Directory and File Commands](Using%20Combined%20Directory%20and%20File%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqmrsgqwvgvzr) describes commands that can be used on both files and directories.
- [Using Fork Commands](Using%20Fork%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqmrsguwvgvzr) describes the commands to interact with data forks.
- [Using Desktop Database Commands](Using%20Desktop%20Database%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjufvbuqmrsgywvgvzr) describes the commands to read and write information store in the server's desktop database.

Refer to the following reference document for AFP:

- _Apple Filing Protocol Reference_

The following sources provide additional information that may be of interested to AFP developers:

- _Inside AppleTalk_. Addison Wesley. ISBN 0-201-19257-8.
- _Applied Cryptography, Second Edition_, by Bruce Schneier. Specifically, the chapter on Diffie-Hellman Key Exchange.
[Next](Apple%20Filing%20Protocol%20Concepts.md)

