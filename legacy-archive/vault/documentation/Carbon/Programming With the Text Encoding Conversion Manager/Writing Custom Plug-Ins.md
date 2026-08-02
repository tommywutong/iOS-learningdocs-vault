---
title: Programming With the Text Encoding Conversion Manager
apple_id: TP40000932
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgWithTECM/tecmgr_plugins/tecmgr_plugins.html
archived_at: '2026-07-15T05:24:12.155640Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming With the Text Encoding Conversion Manager](Introduction%20to%20Programming%20With%20the%20Text%20Encoding%20Conversion%20Manager.md)


[Next](Character%20Encodings%20and%20Internet%20Names.md)[Previous](Character%20Encoding%20Concepts%20In-Depth.md)

# Writing Custom Plug-Ins

This document provides information on writing plug-ins for text encoding conversion on Mac OS–based computers.

Text encoding conversion plug-ins, which provide conversion services between pairs of encodings, inform the Text Encoding Conversion Manager about their conversion and encoding analysis capabilities. The Text Encoding Conversion Manager sets up plug-ins and tears them down; the plug-ins perform conversions, handle caller options, and examine text encodings.

Support for new encodings is provided by writing new text encoding plug-ins. Plug-ins are implemented as Code Fragment Manager (CFM) libraries.

The number and kind of text encodings that the Text Encoding Conversion Manager supports depends on the conversion plug-ins that are currently installed in the system. Text encoding conversion plug-ins are installed in the Text Encodings folder within the System Folder.

Generally, plug-ins provide algorithmic conversions, although plug-ins can also provide mapping-table-based conversions. Mapping-table-based conversions provided by the Unicode Converter are available through a provided plug-in which calls the Unicode Converter.

The Text Encoding Conversion Manager provides mechanisms to create converter objects to communicate with the plug-ins.

Plug-ins are implemented as code fragments. The main export symbol of the code fragment is a routine that returns the address of a structure of type `TECPluginDispatchTable`. The structure is a plug-in dispatch table that contains a dispatch table format version number, a signature for the plug-in, and hooks for the methods each plug-in needs to support.

The filename of a plug-in does not affect the actual text conversion performed by the Text Encoding Conversion Manager.

Export symbols of the code fragment plug-in include the standard CFM initialization and termination routines as well as the main routine.

The initialization routine is called by the Text Encoding Conversion Manager when the plug-in is loaded. It must return `noErr` or the plug-in is not installed. For example,

```
OSErr INIT_KoreanPlugin(InitBlockPtr initBlkPtr){
return noErr;
}
```

The termination routine performs cleanup before the plug-in is unloaded. For example,

```
void TERM_KoreanPlugin(void)
{
}
```

The main export symbol is the name of the routine that returns the address of the `TECPluginDispatchTable`. Because this is the main export symbol, the table is loaded after the plug-in has been installed by the Text Encoding Conversion Manager. For example,

```
TECPluginDispatchTable *GetKoreanDispatchTable(void)
{
return &KoreanPluginDispatchTable;
}
```

The table consists of a dispatch table format version number, a signature that uniquely identifies the plug-in, and routine pointers to the plug-in’s methods. The methods are discussed later in this appendix. The compatible version number is always less than or equal to the current version number.

```
struct TECPluginDispatchTable {
    /* version information */
    TECPluginVersion                version;
    TECPluginVersion                compatibleVersion;
    TECPluginSignature              PluginID;

    /* converter hooks */
    TECPluginNewEncodingConverterPtr                                        PluginNewEncodingConverter;
    TECPluginClearContextInfoPtr                                        PluginClearContextInfo;
    TECPluginConvertTextEncodingPtr                                         PluginConvertTextEncoding;
    TECPluginFlushConversionPtr                                         PluginFlushConversion;
    TECPluginDisposeEncodingConverterPtr                                        PluginDisposeEncodingConverter;

    /* sniffer hooks */
    TECPluginNewEncodingSnifferPtr                                      PluginNewEncodingSniffer;
    TECPluginClearSnifferContextInfoPtr                                         PluginClearSnifferContextInfo;
    TECPluginSniffTextEncodingPtr                                       PluginSniffTextEncoding;
    TECPluginDisposeEncodingSnifferPtr                                          PluginDisposeEncodingSniffer;

    /* Support encoding information. These hooks can be implemented as resources. */
    TECPluginGetCountAvailableTextEncodingsPtr
                                            PluginGetCountAvailableTextEncodings;
    TECPluginGetCountAvailableTextEncodingPairsPtr
                                            PluginGetCountAvailableTextEncodingPairs;
    TECPluginGetCountDestinationTextEncodingsPtr
                                            PluginGetCountDestinationTextEncodings;
    TECPluginGetCountSubTextEncodingsPtr                                        PluginGetCountSubTextEncodings;
    TECPluginGetCountAvailableSniffersPtr                                       PluginGetCountAvailableSniffers;
    TECPluginGetCountWebEncodingsPtr                                        PluginGetCountWebTextEncodings;
    TECPluginGetCountMailEncodingsPtr                                       PluginGetCountMailTextEncodings;

    TECPluginGetTextEncodingInternetNamePtr PluginGetTextEncodingInternetName;
    TECPluginGetTextEncodingFromInternetNamePtr
                                            PluginGetTextEncodingFromInternetName;
};
typedef struct TECPluginDispatchTable TECPluginDispatchTable;
```

Each plug-in must implement routines for creating the converter object, resetting the state of the converter object, encoding conversions, and disposing of the converter object. That is, the following routine pointers in the dispatch table should be valid for a basic plug-in:

```
TECPluginNewEncodingConverterPtr
TECPluginClearContextInfoPtr
TECPluginConvertTextEncodingPtr
TECPluginDisposeEncodingConverterPtr

/* You can implement the following routine pointers or use their corresponding  resources. */
TECPluginGetCountAvailableTextEncodingsPtr
TECPluginGetCountAvailableTextEncodingPairsPtr
TECPluginGetCountDestinationTextEncodingsPtr
```

Example:

```
TECPluginDispatchTable KoreanPluginDispatchTable = {
    kTECPluginDispatchTableCurrentVersion,
    kTECPluginDispatchTableCurrentVersion,
    kTECKoreanPluginSignature,

&ConverterPluginNewEncodingConverter, &ConverterPluginClearContextInfo,
&ConverterPluginConvertTextEncoding,
&ConverterPluginFlushConversion,
&ConverterPluginDisposeEncodingConverter,

&ConverterPluginNewEncodingSniffer,
&ConverterPluginClearSnifferContextInfo,
&ConverterPluginSniffTextEncoding,
&ConverterPluginDisposeEncodingSniffer,

nil, // &ConverterPluginGetAvailableTextEncodings,
nil, // &ConverterPluginGetAvailableTextEncodingPairs,
nil, // &ConverterPluginGetDestinationTextEncodings,
nil, // PluginGetSubTextEncodings,

nil, // PluginGetSniffers;
nil, // PluginGetWebTextEncodings;
nil, // PluginGetMailTextEncodings;

nil, // PluginGetTextEncodingMIMEName,
nil, // PluginGetTextEncodingFromMIMEName,
};
```

The Text Encoding Conversion Manager communicates with its plug-ins through structures of type `TECConverterContextRec`. Context structures are created and disposed of by the Text Encoding Conversion Manager. Plug-ins are called to construct and dispose of their own data. The Text Encoding Conversion Manager and plug-ins communicate with each other in the following ways:

1. The Text Encoding Conversion Manager supplies input and output buffers to plug-ins.
2. Plug-ins report back how much text they have converted.

```
struct TECConverterContextRec {
    /* public - manipulated externally and within plug-in   */
    Ptr pluginRec;
    TextEncoding sourceEncoding;
    TextEncoding destEncoding;
    UInt32 reserved1;
    UInt32 reserved2;
    TECBufferContextRec bufferContext;

    /* private - manipulated only within plug-in */
    UInt32 contextRefCon;
    ProcPtr conversionProc;
    ProcPtr flushProc;
    ProcPtr clearContextInfoProc;
    UInt32 options1;
    UInt32 options2;
    TECPluginStateRec pluginState; /* state information */
};
typedef struct TECConverterContextRec TECConverterContextRec;
```

Most of the public section of the `TECConverterContextRec` structure is maintained by the Text Encoding Conversion Manager and should not be modified by the plug-in. The `bufferContext` field is set up by the Text Encoding Conversion Manager to point to the input and output buffers before the conversion routine, pointed to by `PluginConvertTextEncoding` (a routine pointer defined in the plug-in dispatch table), is called. On exit from that routine, the plug-in should update this structure to indicate how much of the input buffer was consumed and how much text was placed in the output buffer.

```
struct TECBufferContextRec {
    TextPtr textInputBuffer;
    TextPtr textInputBufferEnd;
    TextPtr textOutputBuffer;
    TextPtr textOutputBufferEnd;
    TextPtr encodingInputBuffer;                        /* currently not used */
    TextPtr encodingInputBufferEnd; /* currently not used */
    TextPtr encodingOutputBuffer; /* currently not used */
    TextPtr encodingOutputBufferEnd; /* currently not used */
};
typedef struct TECBufferContextRec TECBufferContextRec;
```

The private section of the `TECConverterContextRec` structure provides persistent storage for a plug-in between conversion routine calls. It isn’t modified by the Text Encoding Conversion Manager. For example, the private section can be used to store state information during a multi-pass encoding conversion. If a plug-in requires more space than is provided in this structure to keep its local data, it can maintain a pointer or a handle to its data in the `contextRefCon` field.

The fields in the private section can be used in any way a particular plug-in requires. All current Apple plug-ins set up these fields with the routine pointed to by `PluginNewEncodingConverter`, a routine pointer defined in the plug-in dispatch table, in the following way:

The `contextRefCon` field is set to `nil`. It can be used to store a handle to additional information handled by the plug-in.

The `conversionProc` field points to a routine within the plug-in that performs a specific conversion, for example, EUC to ISO-2022-JP.

The `flushProc` field points to a routine within the plug-in that flushes the output buffer with some text sequence in order to set the output buffer state to a certain text mode, such as ASCII mode. It is currently used in EUC to ISO-2022-JP conversion.

The `clearContextInfoProc` field points either to a generic routine that clears all state information in the private section or to custom routines that clear the conversion context for each specific conversion.

Only `state1`, `state2`, `state3`, and `state4` of the `TECPluginStateRec` structure are used for storing plug-in state information. But you can use the rest in any way you want.

```
struct TECPluginStateRec {
UInt8 state1;
UInt8 state2;
UInt8 state3;
UInt8 state4;
UInt32 longState1;
UInt32 longState2;
UInt32 longState3;
UInt32 longState4;
};
typedef struct TECPluginStateRec TECPluginStateRec;
```

When a converter object is created, the creation routine pointed to by `PluginNewEncodingConverter`, a routine pointer defined in the plug-in dispatch table, is called by the Text Encoding Conversion Manager to allow the plug-in to set up its `TECConverterContextRec` structure. This creation routine sets up the conversion routine pointer, clear context information routine pointer, flush routine pointer, and the context reference value.

The `TECConverterContextRec` structure needs to contain all the information the plug-in required to perform conversions between the encodings specified in `inputEncoding` and `outputEncoding`.

Note that text encoding specifications (type `TextEncoding`) are considered private structures. They are defined as of type `UInt32` and can be passed by value. Text encoding specifications are persistent objects. For example,

```swift
static OSStatus ConverterPluginNewEncodingConverter(
    TECObjectRef *newEncodingConverter,
    TECConverterContextRec *plugContext,
    TextEncoding inputEncoding,
    TextEncoding outputEncoding)
{
#pragma unused( newEncodingConverter )

    OSStatus status = noErr;
    TextEncoding encodingKSC_5601_87 = CreateTextEncoding(kTextEncodingKSC_5601_87,
            kTextEncodingDefaultVariant, kTextEncodingDefaultFormat);
    TextEncoding encodingISO_2022_KR =
         CreateTextEncoding(kTextEncodingISO_2022_KR,
            kTextEncodingDefaultVariant, kTextEncodingDefaultFormat);
    TextEncoding encodingEUC_KR = CreateTextEncoding(kTextEncodingEUC_KR,
            kTextEncodingDefaultVariant, kTextEncodingDefaultFormat);
    TextEncoding encodingMacKorean =
         CreateTextEncoding(kTextEncodingMacKorean,
            kTextEncodingDefaultVariant, kTextEncodingDefaultFormat);

    /* initialize private data in plugContext */
    plugContext->conversionProc = nil;
    plugContext->clearContextInfoProc = nil;
    plugContext->flushProc = nil;
    plugContext->contextRefCon = (unsigned long)nil;

    /* create the converter if possible */
    if (inputEncoding == encodingKSC_5601_87) {

        if (outputEncoding == encodingEUC_KR || outputEncoding == encodingMacKorean) {
            plugContext->conversionProc = (ProcPtr) &ConvertKSC_5601toEUC_KR;
            plugContext->clearContextInfoProc = (ProcPtr) &ClearConverterContext;
        } else{
            status = kTextUnsupportedEncodingErr;
        }

    } else if (inputEncoding ==  encodingISO_2022_KR) {
        if (outputEncoding == encodingEUC_KR || outputEncoding == encodingMacKorean) {
            plugContext->conversionProc = (ProcPtr) &ConvertISO2022KRtoEUC_KR;
            plugContext->clearContextInfoProc = (ProcPtr) &ClearConverterContext;
    } else {
        status = kTextUnsupportedEncodingErr;
        }
    } else if (inputEncoding ==  encodingEUC_KR ||
                inputEncoding == encodingMacKorean) {

    if (outputEncoding == encodingKSC_5601_87) {
        plugContext->conversionProc = (ProcPtr) &ConvertEUC_KRtoKSC_5601;
        plugContext->clearContextInfoProc = (ProcPtr) &ClearConverterContext;
    } else if (outputEncoding == encodingISO_2022_KR) {
        plugContext->conversionProc = (ProcPtr) &ConvertEUC_KRtoISO2022KR;
        plugContext->clearContextInfoProc = (ProcPtr) &ClearConverterContext;
        plugContext->flushProc = (ProcPtr) &FlushTextEUC_KRtoISO_2022_KR;
    } else{status = kTextUnsupportedEncodingErr;
    }
    } else {
        status = kTextUnsupportedEncodingErr;
    }
    return status;
    }
```

The clear context routine pointed to by `PluginClearContextInfo`, a routine pointer defined in the plug-in dispatch table, is called to clear out the plug-in context or state information to prepare for a new conversion of the same type. It is always called by the Text Encoding Conversion Manager right after creating the converter object. For example,

```swift
static OSStatus ConverterPluginClearContextInfo(
TECObjectRef encodingConverter,
TECConverterContextRec *plugContext)
{
OSStatus status = noErr;
status = (
*((TECPluginClearContextInfoPtr) (plugContext->clearContextInfoProc))
) (encodingConverter, plugContext);
return status;
}
```

The pointer `plugContext->clearContextInfoProc` points to a clear context routine. It is set up in the `ConverterPluginNewEncodingConverter` routine above when a converter object is created. For example,

```swift
OSStatus ClearConverterContext(
TECObjectRef encodingConverter,
TECConverterContextRec *plugContext)
{
#pragma unused (encodingConverter)
OSStatus status = noErr;
if (plugContext)
{

// for normal state
plugContext->pluginState.state1 = kASCIIState;

// for shift in/out state
plugContext->pluginState.state2 = kShiftInState;

// for saved byte
plugContext->pluginState.state3 = kNullSaveByte;

// for pure KSC <-> EUC conversion
plugContext->pluginState.state4 = kKSC5601_92State;
plugContext->pluginState.longState1 = 0;
plugContext->pluginState.longState2 = 0;
plugContext->pluginState.longState3 = 0;
plugContext->pluginState.longState4 = 0;
}

else
{
status = paramErr;
}
return status;
}
```

Note that you may directly call a particular `ClearConverterContext` routinein the `ConverterPluginClearContextInfo` routine for clearing the converter context if you don’t care what the conversion is. The Text Encoding Conversion Manager provides a convenient way, using the routine pointer `plugContext->clearContextInfoProc`, to call a clear context routine that is set up according to the input and output encodings when the converter object is created.

The conversion routine pointed to by `PluginConvertTextEncoding`, a routine pointer defined in the plug-in dispatch table, is called to perform the actual encoding conversion.

The `bufferContext` field of a structure of type `TECBufferContextRec`—used for the `TECConverterContextRec` parameter of the conversion routine—points to the beginning and end of the input and output buffers.

The plug-in should convert the text in the input buffer to the desired encoding and place it in the output buffer, deciding how much of the input text it can convert and fit in the output buffer. Upon exit, the plug-in needs to update the `inputBuffer` and `outputBuffer` pointers to reflect how much of the text was converted an how large the output was. The plug-in should save all necessary state information so that it can continue the conversion where it left off in the event that all of the input text could not fit, after conversion, in the output buffer. When converting the text, convert as much of the input text as you can and still fit the converted text in the output buffer. For example,

```swift
static OSStatus ConverterPluginConvertTextEncoding(
TECObjectRef encodingConverter, TECConverterContextRec *plugContext)
{
OSStatus status = noErr;

status =  (
*((TECPluginConvertTextEncodingPtr) (plugContext->conversionProc)))

(encodingConverter, plugContext);
return status;
}
```

The pointer `plugContext->conversionProc` points to a encoding conversion routine. It is setup in the `ConverterPluginNewEncodingConverter` routine above when a converter object is created. For example,

```swift
OSStatus ConvertISO2022KRtoEUC_KR(
TECObjectRef encodingConverter, TECConverterContextRec *plugContext)
{
#pragma unused (encodingConverter)
OSStatus status = noErr;

if (plugContext) {
BytePtr inBuf  = plugContext->bufferContext.textInputBuffer;
BytePtr inEnd  = plugContext->bufferContext.textInputBufferEnd;
BytePtr outBuf = plugContext->bufferContext.textOutputBuffer;
BytePtr outEnd = plugContext->bufferContext.textOutputBufferEnd;
Byte saveByte;
UInt8 escState, shiftState;

/* get state information */
escState = plugContext->pluginState.state1;
shiftState = plugContext->pluginState.state2;
saveByte = plugContext->pluginState.state3;

/* perform conversion */
/* no error message yet if there is no input */
while ((inBuf < inEnd) && (status == noErr))
{
status = HandleState(*inBuf, &escState, &shiftState,
&saveByte, &outBuf, outEnd);

/* Check if the buffer full status is actually */
/* a buffer below minimum size error. */
/* And advance the input buffer if appropriate. */
PostProcess(plugContext->bufferContext.textOutputBuffer,
outBuf, &inBuf, inEnd, &escState, &status);
}
/* save state information */
plugContext->pluginState.state1 = escState;
plugContext->pluginState.state2 = shiftState;
plugContext->pluginState.state3 = saveByte;

/* save new buffer positions */
plugContext->bufferContext.textOutputBuffer = outBuf;
plugContext->bufferContext.textInputBuffer  = inBuf;
}

else
{
status = paramErr;
}

return status;
}
```

Note that you may not directly use the `ConverterPluginConvertTextEncoding` routine for converting the encodings because you don’t have the conversion information. The Text Encoding Conversion Manager provides a convenient way to call a conversion routine that is set up according to the input and output encodings.

The destruction routine pointed to by `PluginDisposeEncodingConverter`, a routine pointer defined in the plug-in dispatch table, is called for each plug-in referenced in a converter object when it is disposed of. The plug-in is responsible for disposing of any memory or other resources such as conversion tables it may have created or loaded from disk in the creation routine. For example,

```
static OSStatus ConverterPluginDisposeEncodingConverter(
TECObjectRef newEncodingConverter,
TECConverterContextRec *plugContext)
{
OSStatus status = noErr;
return status;
}
```

The flush routine pointed to by `PluginFlushConversion`, a routine pointer defined in the plug-in dispatch table, is called to flush the output buffer to certain mode. For example, this is needed in the `EUC_KR` to `ISO2022_KR` conversion because after an input buffer has been consumed, a shift in sequence may be needed to change back to ASCII mode in the output buffer.

```swift
OSStatus FlushTextEUC_KRtoISO_2022_KR(
TECObjectRef encodingConverter,
TECConverterContextRec *plugContext)
{
#pragma unused( encodingConverter )

OSStatus status = noErr;

if (plugContext)
{
BytePtr outBuf = plugContext->bufferContext.textOutputBuffer;
BytePtr outEnd = plugContext->bufferContext.textOutputBufferEnd;
UInt8 isoState, shiftState;
Byte saveByte;

isoState = plugContext->pluginState.state1;
shiftState = plugContext->pluginState.state2;
saveByte = plugContext->pluginState.state3;
if (shiftState != kShiftInState) {
/* Shift in sequence */
status = OutputEscapeSequence(
kShiftInState, &outBuf, outEnd);

if (status == noErr)
{

/* Remember to reset back to shift in mode if no error */
isoState = kDesignationState;
shiftState = kShiftInState;
saveByte = kNullSaveByte;
}

/* Check if the buffer full status is actually */
/* a buffer below minimum size error */
if ((status == kTECOutputBufferFullStatus) &&
(outBuf == plugContext->bufferContext.textOutputBuffer))
status = kTECBufferBelowMinimumSizeErr;

/* Save state information & new buffer positions */
plugContext->pluginState.state1 = isoState;
plugContext->pluginState.state2 = shiftState;
plugContext->pluginState.state3 = saveByte;
plugContext->bufferContext.textOutputBuffer = outBuf;
}
}

else
{
status = paramErr;
}

return status;
}
```

The following routines, defined in the plug-in dispatch table, provide information to the Text Encoding Conversion Manager to find out what services are available to it in each of its plug-ins. These services include which encodings the plug-in knows about and which conversions it can perform on those encodings.

Some routines may be replaced by resources. Resources are preferable. However, in some cases, you might want to use the routines—for example, for the Unicode plug-in, which needs to scan tables.

The routine pointed to by `PluginGetCountAvailableTextEncodings`, a routine pointer defined in the plug-in dispatch table, counts the actual number of available text encodings and fills in an array of type `TextEncoding` with the encodings supported by the plug-in. This is used by the `TECGetAvailableTextEncodings` routine in the Text Encoding Conversion Manager.

```
typedef OSStatus (*TECPluginGetCountAvailableTextEncodingsPtr)
(TextEncoding *availableEncodings,
ItemCount maxAvailableEncodings,
ItemCount *actualAvailableEncodings);
```

The routine pointed to by `PluginGetCountAvailableTextEncodingPairs`, a routine pointer defined in the plug-in dispatch table, counts the actual number of available text encoding conversions and fills in an array of type `TECConversionInfo` with the encoding conversions supported by the plug-in. This is used by the `TECGetAvailableTextEncodings` routine in the Text Encoding Conversion Manager.

```
typedef OSStatus (*TECPluginGetCountAvailableTextEncodingPairsPtr)
(TECConversionInfo *availableEncodings,
ItemCount maxAvailableEncodings,
ItemCount *actualAvailableEncodings);
```

A `TECConversionInfo` structure is used to describe conversion services available in a plug-in. Each plug-in is required to provide information about the actual encoding conversions in a given buffer. This is used by `TECGetDirectTextEncodingConversions` in the Text Encoding Conversion Manager.

```
struct TECConversionInfo {
TextEncoding sourceEncoding;
TextEncoding destinationEncoding;
UInt16 reserved1;
UInt16 reserved2;
};
```

Each structure contains a pair of source and destination encodings that describes the kind of conversion the plug-in can perform. An encoding is created by using the `CreateTextEncoding` function. For example,

```
TextEncoding encodingKSC_5601_87 = CreateTextEncoding(
kTextEncodingKSC_5601_87,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat
);
```

The variant and format are discussed in conjunction with the resource of type `kTECAvailableEncodingsResType` later in this appendix.

The routine pointed to by `PluginGetCountDestinationTextEncodings`, a routine pointer defined in the plug-in dispatch table, counts the actual number of available destination text encodings. The routine also fills in an array of type `TextEncoding` with all the text encodings that the parameter `inputEncoding` can be directly converted to in one step. This routine is used by the Text Encoding Conversion Manager to find and evaluate paths from one encoding to another.

```
typedef OSStatus (*TECPluginGetCountDestinationTextEncodingsPtr)
(TextEncoding inputEncoding,
TextEncoding *destinationEncodings,
ItemCount maxDestinationEncodings,
ItemCount *actualDestinationEncodings
);
```

The routine pointed to by `PluginGetCountSubTextEncodings`, a routine pointer defined in the plug-in dispatch table, finds out which subencodings are packaged within a text encoding. For example EUC-JP and ISO 2022-JP both contain JIS X0208, JIS X0212, JIS Roman, and half-width Katakana.

```
typedef OSStatus (*TECPluginGetCountSubTextEncodingsPtr)
(TextEncoding inputEncoding,
TextEncoding subEncodings[],
ItemCount maxSubEncodings,
ItemCount *actualSubEncodings);
```

The routine pointed to by `PluginGetCountAvailableSniffers`, a routine pointer defined in the plug-in dispatch table, counts the actual number of available sniffers and fills in an array of type `TextEncoding` with the encodings that can be sniffed by the plug-in.

```
typedef OSStatus (*TECPluginGetCountAvailableSniffersPtr)
(TextEncoding *availableEncodings,
ItemCount maxAvailableEncodings,
ItemCount *actualAvailableEncodings);
```

The routine pointed to by `PluginGetTextEncodingInternetName`, a routine pointer defined in the plug-in dispatch table, finds the name of a text encoding as it would appear in a Multipurpose Internet Mail Extensions (MIME) header. The routine pointed to by `PluginGetTextEncodingFromInternetName` performs the inverse.

```
typedef OSStatus (*TECPluginGetTextEncodingInternetNamePtr)
(TextEncoding textEncoding,
Str255 encodingName);
typedef OSStatus (*TECPluginGetTextEncodingFromInternetNamePtr)
(TextEncoding *textEncoding,
ConstStr255Param encodingName);
```

The routine pointed to by `PluginGetCountWebTextEncodings`, a routine pointer defined in the plug-in dispatch table, counts the actual number of available Web encodings and fills in an array of type `TextEncoding` with the Web encodings. These encodings might appear in a Web browser encoding menu.

```
typedef OSStatus (*TECPluginGetCountWebEncodingsPtr)
(TextEncoding *availableEncodings,
ItemCount maxAvailableEncodings,
ItemCount *actualAvailableEncodings);
```

The routine pointed to by `PluginGetCountMailTextEncodings`, a routine pointer defined in the plug-in dispatch table, counts the actual number of available mail encodings and fills in an array of type `TextEncoding` with the mail encodings. These encodings might appear in an email transfer encoding menu.

```
typedef OSStatus (*TECPluginGetCountMailEncodingsPtr)
(TextEncoding *availableEncodings,
ItemCount maxAvailableEncodings,
ItemCount *actualAvailableEncodings);
```

To facilitate plug-in development, avoid duplicate code, and eventually avoid unnecessarily loading a plug-in, certain data access plug-in methods can be implemented as resources. If these resources are present, the corresponding routines are never called. If this information is not available until runtime, such as is the case with the Unicode plug-in, which needs to find out which conversion tables are available, then the plug-in is loaded and the corresponding routine is called instead. If all of these are implemented as resources, then initialization of the Text Encoding Conversion Manager occurs more quickly because you don’t need to load your plug-in fragment until it is required.

All resource IDs are `kTECResourceID`.

| Resource macro | Replaces Routines |
| --- | --- |
| `kTECAvailableEncodingsResType` | `PluginGetCountAvailableTextEncodings` |
| `kTECConversionInfoResType` | `PluginGetCountAvailableTextEncodingPairs` |
|  | `PluginGetCountDestinationTextEncodings` |
| `kTECInternetNamesResType` | `PluginGetTextEncodingInternetName PluginGetTextEncodingFromInternetName` |
| `kTECLocalizedNamesResType` | `PluginGetTextEncodingLocalizedName` |
| `kTECAvailableSniffersResType` | `PluginGetCountAvailableSniffers` |
| `kTECWebEncodingsResType` | `PluginGetCountWebTextEncodings` |
| `kTECMailEncodingsResType` | `PluginGetCountMailTextEncodings` |
| `kTECSubTextEncodingsResType` | `PluginGetCountSubTextEncodings` |

The above resources are discussed below.

The following resource type provides information that tells which encodings the plug-in knows about.

```
/* supported encodings list */

type kTECAvailableEncodingsResType {
    longint = $$CountOf (memberArray);
    Array memberArray {
        memberStart:
        TECTextEncoding             /* encoding */
        memberEnd:
    };
};
```

For example,

```
resource kTECAvailableEncodingsResType (kTECResourceID) {
{
kTextEncodingKSC_5601_87, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingISO_2022_KR, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingMacKorean,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingEUC_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
}
};
```

The above example shows that there are four encodings, namely, `kTextEncodingKSC_5601_87`, `kTextEncodingISO_2022_KR`, `kTextEncodingMacKorean`, and `kTextEncodingEUC_KR`, that this plug-in knows about. Since the encodings do not have special variants and formats, default variants and formats are used. If a plug-in supports different variants and formats, the text encodings must appear in the list.

The first value in the resource entries above, `kTextEncodingKSC_5601_87 (0x0640)`, with type `TextEncodingBase` (`UInt32`), as defined in `TextCommon.h`, is the primary specification of the source or destination encoding. The values 0 through 32 (0x00 through 0x0020) correspond to Mac OS script codes.

The second value, with type `TextEncodingVariant` (`UInt32`), specifies the minor variant of the base encoding. For a given `TextEncodingBase`, the enumeration of variants always begins with 0. The value `kTextEncodingDefaultVariant` specifies the default variant of the base encoding.

The last value, with type `TextEncodingFormat` (`UInt32`), designates a particular way of algorithmically transforming a particular encoding, say for transmission through communication channels that may handle only 7-bit values. These transformations are not viewed as different encodings, but merely as different formats for representing the same encoding. The value `kTextEncodingDefaultFormat` specifies the default format of the base encoding.

The following resource type provides information identifying which encoding conversions the plug-in can perform.

```
/* Conversion pairs */
type kTECConversionInfoResType {
    longint = $$CountOf (memberArray);
    Array memberArray {
        memberStart:
        TECTextEncoding                     /* source encoding */
        TECTextEncoding                     /* dest encoding */

        longint res1;      /* reserved - free */
        longint res2;      /* reserved - free   */
        memberEnd:
    };
};
```

For example,

```
resource kTECConversionInfoResType (kTECResourceID) {
{
/* Round trip KSC 5601 to MacKorean */
kTextEncodingKSC_5601_87, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingMacKorean, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat, 0, 0, kTextEncodingMacKorean,
kTextEncodingDefaultVariant, kTextEncodingDefaultFormat,
kTextEncodingKSC_5601_87, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat, 0, 0,

/* Round trip ISO 2022 to MacKorean */
kTextEncodingISO_2022_KR, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingMacKorean, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat, 0, 0, kTextEncodingMacKorean,
kTextEncodingDefaultVariant, kTextEncodingDefaultFormat,
kTextEncodingISO_2022_KR, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat, 0, 0,
...
}
};
```

The following resource type provides the name of a text encoding as it would appear in a Multipurpose Internet Mail Extensions (MIME) header. Multiple encodings can map to one Internet MIME name, but an Internet MIME name maps only to the first encoding found.

```
/* Internet names */

type kTECInternetNamesResType {
    longint = $$CountOf (memberArray);
    Array memberArray {

    memberStart:
    ListStart:
    longint = (ListEnd[$$ArrayIndex(memberArray)] -
        ListStart[$$ArrayIndex(memberArray)]) / 8 - 4;
                                    /* offset to next item */
    TECTextEncoding                                 /* text encoding of name */
    pstring;                                        /* encoding name */
    align long;                                 /* match size to C structure size */

    ListEnd:
    memberEnd:
    };
};
```

For example,

```
resource kTECInternetNamesResType (kTECResourceID) {
{
kTextEncodingKSC_5601_87, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
"KS_C_5601-1987",
kTextEncodingKSC_5601_87, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
"KSC_5601",
kTextEncodingISO_2022_KR, kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
"ISO-2022-KR",
kTextEncodingEUC_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
"EUC-KR”
}
};
```

The above example shows that there are three encodings, namely, `kTextEncodingKSC_5601_87`, `kTextEncodingISO_2022KR`, and `kTextEncodingEUC_KR`, for which this plug-in knows the Internet names. Because the encodings do not have special variants and formats, default variants and formats are used. One of the encodings, `kTextEncodingKSC_5601_87`, has two Internet names, namely, `KS_C_5601-1987` and `KSC_5601`.

The following resource type provides information about the available sniffers.

```
/* supported sniffers list */
type kTECAvailableSniffersResType {
    longint = $$CountOf (memberArray);
    Array memberArray {
    memberStart:
    TECTextEncoding /* encoding */
    memberEnd:
    };
};
```

For example,

```
resource kTECAvailableSniffersResType (kTECResourceID) {
{
kTextEncodingKSC_5601_87, kTextEncodingDefaultVariant, kTextEncodingDefaultFormat, kTextEncodingISO_2022_KR, kTextEncodingDefaultVariant, kTextEncodingDefaultFormat,
kTextEncodingEUC_KR, kTextEncodingDefaultVariant, kTextEncodingDefaultFormat,
}
};
```

The following resource type provides information about the available Web encodings.

```
/* Web encodings */
type kTECWebEncodingsResType {
    longint = $$CountOf (memberArray);                              /* number of sets in resource */
    Array memberArray {
        memberStart:
        ListStart:
        longint = (ListEnd[$$ArrayIndex(memberArray)] -
            ListStart[$$ArrayIndex(memberArray)]) / 8 - 4;
                                 /* offset to next item */
        longint = $$CountOf (localesArray);
                                 /* number of encodings in resource */
        Array localesArray {
            TECLocale                       /* search locales */
        };
        longint = $$CountOf (webEncodingsArray);
                                /* number of encodings in resource *
        Array webEncodingsArray {
            TECTextEncoding                 /* Web encodings */
        };
        ListEnd:
        memberEnd:
        };
    };
```

For example,

```
resource kTECWebEncodingsResType (kTECResourceID) {
{

/* Korean encodings */
{
verKorea, /* Korean Republic of Korea */
},

{
kTextEncodingISO_2022_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingEUC_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat
},

}
};
```

The following resource type provides information about the available encodings for electronic mail (e-mail) by region.

```
/* mail encodings */
type kTECMailEncodingsResType {
    longint = $$CountOf (memberArray); /* number of sets in resource */
    Array memberArray {
        memberStart:
        ListStart:
    longint = (ListEnd[$$ArrayIndex(memberArray)] -
        ListStart[$$ArrayIndex(memberArray)]) / 8 - 4;
                                    /* offset to next item */
        longint = $$CountOf (localesArray);
                                    /* number of encodings in resource */
        Array localesArray {
            TECLocale                           /* search locales */
        };
        longint = $$CountOf (mailEncodingsArray);
                                    /* number of encodings in resource */
        Array mailEncodingsArray {
                TECTextEncoding                 /* mail encodings */
        };
        ListEnd:
        memberEnd:
    };
};
```

For example,

```
resource kTECMailEncodingsResType (kTECResourceID) {
{

/* Korean encodings */
{
verKorea, /* Korean Republic of Korea */
},

{
kTextEncodingMacKorean,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingISO_2022_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingEUC_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingUnicodeV2_0,
kTextEncodingDefaultVariant,
kUnicodeUTF7Format,
kTextEncodingUnicodeV2_0,
kTextEncodingDefaultVariant,
kUnicodeUTF8Format
},

}
};
```

The following resource type provides information about which subencodings are packaged within a text encoding. For example ISO 2022-JP and EUC-JP both contain JIS Roman, JIS X0208, JIS X0212, and half-width Katakana.

```
/* subencodings */
type kTECSubTextEncodingsResType {
    longint = $$CountOf (memberArray);
                        /* number of sets of subencodings in resource */
    Array memberArray {
        memberStart:
        ListStart:
    longint = (ListEnd[$$ArrayIndex(memberArray)] -
            ListStart[$$ArrayIndex(memberArray)]) / 8 - 4;
                        /* offset to next item */
    TECTextEncoding                 /* search encoding */
    longint = $$CountOf (subEncodingsArray);
                         /* number of subencodings in resource */

    Array subEncodingsArray {
        TECTextEncoding             /* search encoding */
    };

    ListEnd:
    memberEnd:
    };
};
```

For example,

```
resource kTECSubTextEncodingsResType (kTECResourceID) {
{
kTextEncodingISO_2022_JP,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,

{
kTextEncodingISOLatin1,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingJIS_X0208_90,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingJIS_X0212_90,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,

/* half-width katakana */
kTextEncodingJIS_X0201_76,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
},

kTextEncodingEUC_JP,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,

{
kTextEncodingISOLatin1,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingJIS_X0208_90,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
kTextEncodingJIS_X0212_90,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,

/* half-width katakana */
kTextEncodingJIS_X0201_76,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat,
...
}

}
};
```

Sniffers allow the Text Encoding Conversion Manager to detect the encoding characteristics of a text stream. A context record of the sniffer is provided for plug-ins and Text Encoding Conversion Manager communication. A sniffer is created by the Text Encoding Conversion Manager and the routine pointed to by `PluginNewEncodingSniffer`, a routine pointer defined in the plug-in dispatch table, is called. All sniffer routines are defined in the plug-in dispatch table. They are discussed below.

The sniffer context structure `TECSnifferContextRec` is similar to `TECConverterContextRec`. Its public section contains information set up by the Text Encoding Conversion Manager and returns information to the caller. The private section is available for plug-in use.

```
struct TECSnifferContextRec {
/* public - manipulated externally and by plug-in */
Ptr pluginRec;
TextEncoding encoding;
ItemCount maxErrors;
ItemCount maxFeatures;
TextPtr textInputBuffer;
TextPtr textInputBufferEnd;
ItemCount numFeatures;

/* will be output to caller */
ItemCount numErrors;

/* private - manipulated only within plug-in */
UInt32 contextRefCon;
ProcPtr sniffProc;
ProcPtr clearContextInfoProc;
TECPluginStateRec pluginState; /* state information */
};
typedef struct TECSnifferContextRec TECSnifferContextRec;
```

When a sniffer object is created in the Text Encoding Conversion Manager, the routine pointed to by `PluginNewEncodingSniffer`, a routine pointer defined in the plug-in dispatch table, is called by the Text Encoding Conversion Manager to allow the plug-in to set up its sniffer context structure `TECSnifferContextRec`.

Example:

```swift
OSStatus ConverterPluginNewEncodingSniffer(
TECSnifferObjectRef *encodingSniffer,
TECSnifferContextRec *snifContext,
TextEncoding inputEncoding)
{
#pragma unused (encodingSniffer)
OSStatus status = noErr;

TextEncoding encodingKSC_5601_87 =
CreateTextEncoding(kTextEncodingKSC_5601_87,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat);

TextEncoding encodingISO_2022_KR =
CreateTextEncoding( kTextEncodingISO_2022_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat);

TextEncoding encodingEUC_KR =
CreateTextEncoding( kTextEncodingEUC_KR,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat);

TextEncoding encodingMacKorean =
CreateTextEncoding( kTextEncodingMacKorean,
kTextEncodingDefaultVariant,
kTextEncodingDefaultFormat);

if (snifContext)
{
if (inputEncoding == encodingKSC_5601_87)
snifContext->sniffProc = (ProcPtr) SniffKSC_5601;

else if (inputEncoding == encodingISO_2022_KR)
snifContext->sniffProc = (ProcPtr) SniffISO2022KR;

else if (inputEncoding == encodingEUC_KR ||
inputEncoding == encodingMacKorean)
snifContext->sniffProc = (ProcPtr) SniffEUC_KR;

else
status = kTextUnsupportedEncodingErr;
}

else
{
status = paramErr;
}

return status;
}
```

The routine pointed to by `PluginClearSnifferContextInfo`, a routine pointer defined in the plug-in dispatch table, is called to clear the sniffer context state information for sniffing a new input buffer. This is always called by the Text Encoding Conversion Manager right after creating the sniffer.

Example:

```swift
OSStatus ConverterPluginClearSnifferContextInfo(
TECSnifferObjectRef encodingSniffer,
TECSnifferContextRec *snifContext)
{
#pragma unused (encodingSniffer)
OSStatus status = noErr;

if (snifContext) {
snifContext->pluginState.state1 = kASCIIState;
snifContext->pluginState.state2 = kShiftInState;
snifContext->pluginState.state3 = 0;
snifContext->pluginState.state4 = 0;
snifContext->numFeatures = 0;
snifContext->numErrors   = 0;
}

else
{
status = paramErr;
}

return status;
}
```

The routine pointed to by `PluginSniffTextEncoding`, a routine pointer defined in the plug-in dispatch table, is called to perform the actual sniffing. To sniff text encodings, loop through the input buffer and count errors and features. The Text Encoding Conversion Manager looks at the number of errors and features to determine the encoding of the given text. The routine is pointed to by `snifContext->sniffProc` to `ConverterPluginNewEncodingSniffer`, which is also defined in the plug-in dispatch table, when the sniffer is created. For example,

```swift
OSStatus SniffEUC_KR(
TECSnifferObjectRef encodingSniffer,
TECSnifferContextRec *snifContext)
{
#pragma unused (encodingSniffer)
OSStatus status = noErr;

if (snifContext)
{
BytePtr inputBuffer = snifContext->textInputBuffer;
BytePtr inputBufferEnd = snifContext->textInputBufferEnd;
ItemCount *numErrs = &snifContext->numErrors;
ItemCount maxErrs = snifContext->maxErrors;
ItemCount *numFeatures = &snifContext->numFeatures;
ItemCount maxFeatures = snifContext->maxFeatures;

if (inputBuffer && inputBufferEnd)
{
Byte c;
UInt8 isoState = snifContext->pluginState.state1;
ItemCount errs = *numErrs;
ItemCount features = *numFeatures;

while(errs < maxErrs && features < maxFeatures &&
inputBuffer < inputBufferEnd)
{
c = *inputBuffer++; /* count errors and features in encoding */
/* set status when appropriate */
...
}

/* save state information */
snifContext->pluginState.state1 = isoState;

/* save number of errors and features */
*numErrs = errs;
*numFeatures = features;
} else {
status = paramErr;

/* Initialization.  Just in case. */
*numErrs = 0;
*numFeatures= 0;
}
}

else
{
status = paramErr;
}

return status;
}
```

The destruction routine pointed to by `PluginDisposeEncodingSniffer`, a routine pointer defined in the plug-in dispatch table, is called when the sniffer is disposed of. To dispose of the sniffer, simply dispose of any memory or resources that may have been allocated in the creation routine.

Example:

```
OSStatus ConverterPluginDisposeEncodingSniffer(
TECSnifferObjectRef encodingSniffer,
TECSnifferContextRec *snifContext)
{
#pragma unused (encodingSniffer, snifContext)
/* nothing to do */

return noErr;
}
```

All plug-in routines should return values with `OSStatus` type, except the three routines named by the plug-in library symbols.

Some common status and error codes that may be returned to the Text Encoding Conversion Manager using type `OSStatus` are listed below:

- `kTECOutputBufferFullStatus`—Output buffer is full before all text could be converted.
- `noErr`—No error occurred or status is normal.
- `paramErr`—One or more of the input parameters has an invalid value.
- `kTextUnsupportedEncodingErr`—The given encoding is not supported in the current plug-in.
- `kTECBufferBelowMinimumSizeErr`—The output text buffer is too small to allow processing of the first input text element.
- `kTECPartialCharErr`—The input text ends in the middle of a multi-byte character, conversion stopped. In this case, the plug-in code should save the state in its private space and the input pointer should back up to the beginning of the multi-byte character.
- `kTextMalformedInputErr`—The text input contained a sequence that is not legal in the specified encoding.

The plug-in should have `'encv'` for file creator and '`ecpg`' for file type.

The `'cfrg'` resource serves to inform the Process Manager and Code Fragment Manager of code fragments. The resource ID must be zero.

Example:

```
#ifdef PPC
resource 'cfrg' (0) {

{
kPowerPC, /* instruction set architecture   */
kFullLib, /* base-level library */
kNoVersionNum, /* no implementation version number*/
kNoVersionNum, /* no definition version number */
kDefaultStackSize, /* use default stack size */
kNoAppSubFolder, /* no library directory */
kIsDropIn, /* fragment is a drop-in library */
kOnDiskFlat, /* fragment is in the data fork */
kZeroOffset, /* fragment starts at offset 0 */
kWholeFork, /* fragment occupies entire fork */
"KoreanPlugin" /* name of the library fragment */
}

};

#else
resource 'cfrg' (0) {

{
kMotorola, /* instruction set architecture  */
kFullLib, /* base-level library */
kNoVersionNum, /* no implementation version number*/
kNoVersionNum, /* no definition version number  */
kDefaultStackSize, /* use default stack size */
kNoAppSubFolder, /* no library directory */
kIsDropIn, /* fragment is a drop-in library     */
kOnDiskFlat, /* fragment is in the data fork */
kZeroOffset, /* fragment starts at offset 0 */
kWholeFork, /* fragment occupies entire fork */
"KoreanPlugin" /* name of the library fragment */
};
#endif
```

The `'vers'` resource provides the version information. The resource ID must be 1.

Example:

```
resource 'vers' (1, purgeable)
{
0x01, 0x20, final, 0x00,
verUS,
"1.2",
"1.2, Copyright Apple Computer, Inc. 1994-1997."
};
```

[Next](Character%20Encodings%20and%20Internet%20Names.md)[Previous](Character%20Encoding%20Concepts%20In-Depth.md)

