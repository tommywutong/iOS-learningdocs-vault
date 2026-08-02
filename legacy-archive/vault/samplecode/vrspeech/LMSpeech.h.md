---
title: vrspeech
apple_id: DTS10001034
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrspeech/Listings/LMSpeech_h.html
archived_at: '2026-07-26T19:53:05.140531Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrspeech](vrspeech.md)


[Previous](Common%20Files-QTVRUtilities.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# LMSpeech.h

```
//////////
//
//  File:       LMSpeech.h
//
//  Contains:   Header file and language model BNF for QuickTime VR movies.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1996-1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      12/05/96    rtm     first file
//
//////////

//////////
//
// constants
//
//////////

#define kTopVRLM                    50

#define kVRAllCmd                   100
#define kVRObjCmd                   101
#define kVRPnoCmd                   102

#define kMoveDirAndDeg              500
#define kMoveDirAndRad              501
#define kMoveToNode                 502
#define kZoomDir                    503
#define kSpinStart                  504
#define kSpinStop                   505

// directions
#define kDir                        1000
#define kDirUp                      1001
#define kDirDown                    1002
#define kDirLeft                    1003
#define kDirRight                   1004
#define kDirIn                      1005
#define kDirOut                     1006

// angular displacements
#define kDeg                        1050
#define kAng45                      1051
#define kAng90                      1052
#define kAng135                     1053
#define kAng180                     1054
#define kAng225                     1055
#define kAng270                     1056
#define kAng315                     1057
#define kAng10                      1058
#define kAng36                      1059
#define kUndefinedDegrees           5000

// radian displacements
#define kRad                        1060
#define kRad1PiOver4                1061
#define kRad2PiOver4                1062
#define kRad3PiOver4                1063
#define kRad4PiOver4                1064
#define kRad5PiOver4                1065
#define kRad6PiOver4                1066
#define kRad7PiOver4                1067

// node descriptors
#define kNodeIDNo                   1070
#define kNodeName                   1071

#define kZoom                       200
#define kBAR                        300

//////////
//
// language models
//
//////////

// here is the BNF description of our language models:
//<TopVRLM> {kTopVRLM} = <VRAllLM> | <VRObjLM> | <VRPnoLM>;
//<VRObjLM> {kSRRefCon = kVRObjCmd} =
//          FOO;
//
//<VRPnoLM> {kSRRefCon = kVRPnoCmd} =
//          BAR;

/*

<VRAllLM> {kSRRefCon = kVRAllCmd} =
            <MoveCmd> <MoveDir> <MoveDeg> [degrees] {kMoveDirAndDeg}    |
            <MoveCmd> <MoveDir> <MoveRad> [radians] {kMoveDirAndRad}    |
            <MoveCmd> [to] node <NodeDesc>          {kMoveToNode}       |
            <ZoomCmd> <ZoomDir>                     {kZoomDir}          |
            spin <MoveDir>                          {kSpinStart}        |
            stop [spinning]                         {kSpinStop}         ;

<MoveCmd>  =
            go | move | pan | tilt;

<MoveDir> {kDir} =
            up                  {kDirUp}        |
            down                {kDirDown}      |
            left                {kDirLeft}      |
            right               {kDirRight}     ;

<MoveDeg> {kDeg} =
            ten                 {kAng10}        |
            thirty-six          {kAng36}        |
            forty-five          {kAng45}        |
            ninety              {kAng90}        |
            one thirty-five     {kAng135}       |
            one eighty          {kAng180}       |
            two twenty-five     {kAng225}       |
            two seventy         {kAng270}       |
            three fifteen       {kAng315}       ;

<MoveRad> {kRad}
            = pi over four      {kRad1PiOver4}  |
            pi over two         {kRad2PiOver4}  |
            three pi over four  {kRad3PiOver4}  |
            pi                  {kRad4PiOver4}  |
            five pi over four   {kRad5PiOver4}  |
            three pi over two   {kRad6PiOver4}  |
            seven pi over four  {kRad7PiOver4}  ;

<ZoomCmd> {kSRRefCon = kZoom; kSROptional = true} =
            zoom | go | move;

<ZoomDir> = in                  {kDirIn}        |
            out                 {kDirOut}       |
            forward             {kDirIn}        |
            backward            {kDirOut}       |
            closer              {kDirIn}        |
            farther             {kDirOut}       ;

<NodeDesc> =
            <NodeIDNo> | <NodeName>;

<NodeIDNo> {kNodeIDNo} =
            one | two | three | four | five | six | seven | eight | nine ;

<NodeName> {kNodeName} =
            sample node name;

*/
```

[Previous](Common%20Files-QTVRUtilities.h.md)

