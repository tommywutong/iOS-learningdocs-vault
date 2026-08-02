---
title: CCL Modem Scripting Guide
apple_id: TP40005464
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-06-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Reference/CCLScriptingRef/Introduction/Introduction.html
archived_at: '2026-07-15T07:41:16.407047Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Writing%20a%20CCL%20Script.md)

# Introduction to CCL Modem Scripting Guide

OS X supports communication over telephone lines using Hayes-compatible modems and similar communication channels such as cellular phones. It provides support for these modems using modem scripts.

OS X comes with a number of modem scripts preinstalled. To use OS X with a modem or cellular phone for which a script is not supplied, the user or the modem vendor must either obtain or write a script to control the modem.

Modem scripts are written using the Communication Command Language (CCL). You can create these scripts programmatically using the iSync Plug-in Maker Tool (described in the _[iSync Plug-in Maker User Guide](../../Syncing/iSync%20Plug-in%20Maker%20User%20Guide/Introduction%20to%20iSync%20Plug-in%20Maker%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrr)_) or manually using any text editor.

This guide includes instructions for writing scripts and descriptions of all the CCL commands. It is intended for experienced programmers with a good understanding of telecommunications and modem operation.

The guide is divided into two chapters and two appendixes:

- [Writing a CCL Script](Writing%20a%20CCL%20Script.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqmznknltc) describes the basic elements and structure of a CCL file and the basic tasks a script must perform.
- [CCL Command Reference](CCL%20Command%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnbnknltc) lists the CCL commands, providing for each a definition, syntax, and an example, if appropriate.
- [Result Codes](Result%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqobnknltc) lists result codes returned by the CCL, with a description of the error and the accompanying message, if any.
- [Cable Specifications](Cable%20Specifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnrnknltc) discusses requirements for a CTS/RTS handshaking cable, desirable when using OS X with a 9600 bps or faster modem.

To write a CCL script for OS X, your computer should be running OS X v10.5. For ease of writing scripts, you should also have the latest version of the OS X Developer Tools installed. These provide the iSync Plug-in Maker tool, which makes it easier to create and edit scripts.

For information about the iSync Plug-in Maker, see the _[iSync Plug-in Maker User Guide](../../Syncing/iSync%20Plug-in%20Maker%20User%20Guide/Introduction%20to%20iSync%20Plug-in%20Maker%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrr)_.

You may also find it useful to consult a reference manual on telecommunications and modems, such as _The Complete Modem Reference_ by Gilbert Held, published by John Wiley & Sons, Inc.

A number of modem scripts have already been written for use with OS X. These can be found in the Modem Scripts folder within the user, system, and global Library folders (`/Library/Modem Scripts`, for example). If you have one of the modems for which a script has been provided, you don't need to write a script. You can display a list of the provided scripts from within the iSync Plug-in Maker tool, as described in the _[iSync Plug-in Maker User Guide](../../Syncing/iSync%20Plug-in%20Maker%20User%20Guide/Introduction%20to%20iSync%20Plug-in%20Maker%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrr)_.

If you need to write a script, you may be able to use an existing script as a template. Be sure to use the Save As command to make a copy of the script you're modifying, so that you don't overwrite the original script.

[Next](Writing%20a%20CCL%20Script.md)

