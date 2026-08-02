---
title: TextNameTool
apple_id: DTS10000647
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/TextNameTool/Listings/TextUtilities_c.html
archived_at: '2026-07-18T03:26:40.546770Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextNameTool](TextNameTool.md)


[Next](TextUtilities.h.md)[Previous](PixOps.h.md)

# TextUtilities.c

```c
/*
    File: TextUtilities.c

    Description:
        Routines for simple byte oriented string manipulation
        used in the TextNameTool sample.  

    Copyright:
        Copyright (c) 2003 Apple Computer, Inc. All rights reserved.

    Disclaimer:
        IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc.
        ("Apple") in consideration of your agreement to the following terms, and your
        use, installation, modification or redistribution of this Apple software
        constitutes acceptance of these terms.  If you do not agree with these terms,
        please do not use, install, modify or redistribute this Apple software.

        In consideration of your agreement to abide by the following terms, and subject
        to these terms, Apple grants you a personal, non-exclusive license, under AppleÕs
        copyrights in this original Apple software (the "Apple Software"), to use,
        reproduce, modify and redistribute the Apple Software, with or without
        modifications, in source and/or binary forms; provided that if you redistribute
        the Apple Software in its entirety and without modifications, you must retain
        this notice and the following text and disclaimers in all such redistributions of
        the Apple Software.  Neither the name, trademarks, service marks or logos of
        Apple Computer, Inc. may be used to endorse or promote products derived from the
        Apple Software without specific prior written permission from Apple.  Except as
        expressly stated in this notice, no other rights or licenses, express or implied,
        are granted by Apple herein, including but not limited to any patent rights that
        may be infringed by your derivative works or by other works in which the Apple
        Software may be incorporated.

        The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
        WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
        WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR
        PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE OR IN
        COMBINATION WITH YOUR PRODUCTS.

        IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
        CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
        GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
        ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION
        OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT
        (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN
        ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    Change History (most recent first):
        Wed, Aug 27, 2003 -- created
*/

#include "TextUtilities.h"

#include <stddef.h>
#include <string.h>
#include <ctype.h>










void SetTextRefFromCString(TextReference *tr, char* cstring) {
    tr->strp = (unsigned char*) cstring;
    tr->len = strlen(cstring);
}

void SetTextRefFromHandle(TextReference *tr, Handle h) {
    tr->strp = (unsigned char*) (*h);
    tr->len = GetHandleSize(h);
}

void SetTextRefFromLongTextString(TextReference *tr, LongTextStringPtr textBuffer) {
    *tr = textBuffer->text;
}







OSErr GetDescTextData(AEDesc *theDesc, Ptr *theData, Size *theLength) {
#if TARGET_API_MAC_CARBON
    OSErr err;
    *theLength = AEGetDescDataSize(theDesc);
    *theData = NewPtr(*theLength);
    if (*theData == NULL) return memFullErr;
    err = AEGetDescData(theDesc, *theData, *theLength);
    if (err != noErr) return err;
#else
    *theLength = GetHandleSize((Handle) theDesc->dataHandle);
    *theData = NewPtr(*theLength);
    if (*theData == NULL) return memFullErr;
    BlockMoveData(*theDesc->dataHandle, *theData, *theLength);
#endif
    return noErr;
}


OSErr GetLongTextStringFromDesc(AEDesc *theDesc, LongTextStringPtr *theString) {
    OSErr err;
    LongTextStringPtr localResult;
    Size count;

    localResult = NULL;

#if TARGET_API_MAC_CARBON
    count = AEGetDescDataSize(theDesc);
    localResult = (LongTextStringPtr) NewPtr(offsetof(LongTextString, characters) + count + 1);
    if (localResult == NULL) { err = memFullErr; goto bail; }
    localResult->text.strp = localResult->characters;
    localResult->text.len = count;
    localResult->characters[count] = '\0';
    err = AEGetDescData(theDesc, localResult->text.strp, count);
    if (err != noErr) goto bail;
#else
    count = GetHandleSize((Handle) theDesc->dataHandle);
    localResult = (LongTextStringPtr) NewPtr(offsetof(LongTextString, characters) + count + 1);
    if (localResult == NULL) return memFullErr;
    localResult->text.strp = localResult->characters;
    localResult->text.len = count;
    localResult->characters[count] = '\0';
    BlockMoveData(*theDesc->dataHandle, localResult->text.strp, count);
#endif
    *theString = localResult;
    return noErr;
bail:

    if (localResult != NULL) DisposePtr((Ptr) localResult);
    return err;
}

OSErr GetLongTextStringFromParam(
            const AppleEvent *appleEvt, 
            AEKeyword theAEKeyword, 
            LongTextStringPtr *theString) {
    AEDesc textDesc;
    OSErr err;
    err = AEGetParamDesc(appleEvt, theAEKeyword, typeChar, &textDesc);
    if (err == noErr) {
        err = GetLongTextStringFromDesc(&textDesc, theString);
        AEDisposeDesc(&textDesc);
    }
    return err;
}

OSErr GetLongTextStringFromBuffer(unsigned char *buffer, long bufferLength, LongTextStringPtr *theString) {
    LongTextStringPtr localResult;
    OSErr err;
    localResult = (LongTextStringPtr) NewPtr(offsetof(LongTextString, characters) + bufferLength + 1);
    if (localResult == NULL) {
        err = memFullErr;
    } else {
        localResult->text.strp = localResult->characters;
        localResult->text.len = bufferLength;
        localResult->characters[bufferLength] = '\0';
        if (buffer != NULL) BlockMoveData(buffer, localResult->characters, bufferLength);
        err = noErr;
        *theString = localResult;
    }
    return err;
}



OSErr GetLongTextStringListElt(
            const AEDescList *theAEDescList, 
            long index, 
            LongTextStringPtr *theString) {
    AEDesc textDesc;
    OSErr err;
    AEKeyword theAEKeyword;
    err = AEGetNthDesc(theAEDescList, index, typeChar, &theAEKeyword, &textDesc);
    if (err == noErr) {
        err = GetLongTextStringFromDesc(&textDesc, theString);
        AEDisposeDesc(&textDesc);
    }
    return err;
}



static unsigned char gUpcaseTable[256] = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
    36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 
    53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
    87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 65, 66, 67, 68, 69, 70, 71, 
    72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 
    89, 90, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 
    231, 203, 229, 128, 204, 129, 130, 131, 233, 230, 232, 234, 237, 235, 
    236, 132, 238, 241, 239, 133, 205, 242, 244, 243, 134, 160, 161, 162, 
    163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 
    177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 174, 
    175, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 
    205, 206, 206, 208, 209, 210, 211, 212, 213, 214, 215, 217, 217, 218, 
    219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 
    233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 73, 246, 
    247, 248, 249, 250, 251, 252, 253, 254, 255 };

static unsigned char gIdentityTable[256] = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
    37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 
    54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 
    88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 
    104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
    118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 
    132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 
    146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 
    160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 
    174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 
    188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 
    202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 
    216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 
    230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 
    244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255 };



Boolean SearchTextBuffer(unsigned char *buffer, long bufferLength, 
            unsigned char *pattern, long patternLength,
            long startingPos, Boolean caseSensitive, long* pos) {

    if ( (bufferLength == 0) || (patternLength == 0) || (bufferLength < patternLength) )
        return false;
    else {
        Boolean found, done;
        unsigned char *dataCache, *patBuffer, ch, *allocatedCache, localCache[4096];
        short *matchTable, *mismatchTable;
        long i, j, k, n, end, theValue, array_ix, string_ix, position, dataCacheSize;
        unsigned char *cmap;
            /* get the character mapping table */

            /* calculate cache size */
        if ( caseSensitive ) {
            cmap = gIdentityTable;
            dataCacheSize = sizeof(short)*(256+patternLength-1);
        } else {
            cmap = gUpcaseTable;
            dataCacheSize = sizeof(short)*(256+patternLength-1) + patternLength;
        }
            /* allocate the cache */
        if (dataCacheSize > sizeof(localCache)) {
            allocatedCache = (unsigned char *) NewPtr(dataCacheSize);
            if (allocatedCache == NULL) return false;
            dataCache = allocatedCache;
        } else {
            dataCache = localCache;
            allocatedCache = NULL;
        }
            /* set up our table pointers, make an uppercase pattern if we require one */
        if ( caseSensitive ) {
            patBuffer = pattern;
            mismatchTable = (short*) dataCache;
            matchTable = (short*) (dataCache + (256 * sizeof(short)));
        } else {
            mismatchTable = (short*) dataCache;
            matchTable = (short*) (dataCache + (256 * sizeof(short)));
            patBuffer = (dataCache + sizeof(short) * (256 + patternLength-1));
            for (i=0; i<patternLength; i++) {
                ch = pattern[i];
                patBuffer[i] = cmap[ch];
            }
        }

        /* compute mismatch table.
        mismatch[i] = how far to shift if there is a mismatch on the first
        compare (with string[len-1]) and the character in the text is (code-char i) */
        for (i=0; i<256; i++) mismatchTable[i] = patternLength;
        n = patternLength-1;
        for ( i=0; i<n; i++ )
            mismatchTable[patBuffer[i]] = n - i;

        /* Compute match table
        match[i] = how far to shift if there is a mismatch in the ith position
        of the search string (i < len-1). */
        n = patternLength-1;
        for ( i=0; i<n; i++ ) {
            done = false;
            theValue = patternLength;
            for (end = patternLength-2; ( (end >= 0) && ( ! done ) ) ; --end) {
                for (j=patternLength-1, k=end; ( (k >= 0) && ( ! done ) ) ; --k, --j) {
                    if (i == j) {
                        if (patBuffer[j] != patBuffer[k]) {
                            theValue = patternLength - 1 - end;
                            done = true;
                        }
                        break;
                    }
                    if (patBuffer[j] != patBuffer[k]) break;
                }
                if ( (k < 0) ) { theValue = patternLength - 1 - end; done = true; }
            }
            matchTable[i] = theValue;
        }

        /* perform Boyer-Moore search */
        i = startingPos + patternLength - 1;
        found = false;
        while ( i < bufferLength && ! found ) {

            array_ix = i;
            string_ix = patternLength - 1;

            ch = cmap[buffer[array_ix]];

            if ( ch == patBuffer[string_ix] ) {
                while ( ! found ) {
                    if (--string_ix < 0) {
                        position = i - (patternLength - 1);
                        found = true;
                    } else {
                        --array_ix;
                        ch = cmap[buffer[array_ix]];

                        if ( ch != patBuffer[string_ix] ) {
                            i += matchTable[string_ix];
                            break;
                        }
                    }
                }

            } else i += mismatchTable[ch];
        }

        if (found) *pos = position;

        if (allocatedCache != NULL) DisposePtr((Ptr) allocatedCache);

        return found;
    }
}



Boolean FindLongTextString(LongTextStringPtr theString, 
            unsigned char *pattern, long patternLength,
            long startingPos, Boolean caseSensitive, long* pos) {
    return SearchTextBuffer(theString->text.strp, theString->text.len, pattern, patternLength,
            startingPos, caseSensitive, pos);
}




long CompareTextBuffers(
            unsigned char* bufferA, long bufferAlen, 
            unsigned char* bufferB, long bufferBlen,
            Boolean caseSensitive) {
    long an, bn, i;
    unsigned char *ap, *bp, ac, bc;
    unsigned char *cmap;
    an = bufferAlen;
    ap = bufferA;
    bn = bufferBlen;
    bp = bufferB;
    i = 0;
    if ( caseSensitive ) cmap = gIdentityTable; else cmap = gUpcaseTable;
    while ( ( i < an ) && ( i < bn ) ) {
        ac = cmap[*ap++];
        bc = cmap[*bp++];
        if (ac < bc)
            return -1;
        else if (ac > bc)
            return 1;
        i++;
    }
    if (i < an) return 1;
    if (i < bn) return -1;
    return 0;   
}


long CompareLongTextStringListElt(
            LongTextStringPtr a, 
            LongTextStringPtr b,
            Boolean caseSensitive) {
    return CompareTextBuffers( a->text.strp, a->text.len, b->text.strp, b->text.len, caseSensitive);
}


long CompareLongTextStringListEltToBuffer(
            LongTextStringPtr a, 
            unsigned char* buffer, long bufferlen,
            Boolean caseSensitive) {
    return CompareTextBuffers( a->text.strp, a->text.len, buffer, bufferlen, caseSensitive);
}



void DisposeLongTextString(LongTextStringPtr theString) {
    DisposePtr((Ptr) theString);
}


LongTextStringPtr VSPrintfLongTextString(const char *fmt, va_list args) {

    TextOutputBuffer theBuffer;
    LongTextStringPtr theResult;
    OSErr err;
        /* initial state */
    InitTextBuffer(&theBuffer);
    theResult = NULL;
        /* write to the buffer */
    err = VSPrintfTextBuffer(&theBuffer, fmt, args);
    if (err == noErr) {
            /* save the string */
        err = TextBufferLongTextString(&theBuffer, &theResult);
        if (err != noErr) theResult = NULL;
    }
        /* release the buffer */
    DisposeTextBuffer(&theBuffer);
    return theResult;
}


LongTextStringPtr PrintfLongTextString(const char *fmt, ...) {
    LongTextStringPtr result;
    va_list args;
    va_start(args, fmt);
    result = VSPrintfLongTextString(fmt, args);
    va_end(args);
    return result;
}

OSErr VSPrintfAsXML(TextOutputBuffer *theBuffer, const char *fmt, va_list args) {
    OSErr result;
    TextOutputBuffer messagebuffer;
    LongTextStringPtr messagetext;
    InitTextBuffer(&messagebuffer);
    result = VSPrintfTextBuffer(&messagebuffer, fmt, args);
    if (result == noErr) {
        result = TextBufferLongTextString(&messagebuffer, &messagetext);
        if (result == noErr) {
            result = EncodeXMLTextStringProc(messagetext, theBuffer);
            DisposeLongTextString(messagetext);
        }
        DisposeTextBuffer(&messagebuffer);
    }
    return result;
}

OSErr PrintfAsXML(TextOutputBuffer *theBuffer, const char *fmt, ...) {
    OSErr result;
    va_list args;
    va_start(args, fmt);
    result = VSPrintfTextBuffer(theBuffer, fmt, args);
    va_end(args);
    return result;
}



void InitTextBuffer(TextOutputBuffer *theBuffer) {
    theBuffer->first = theBuffer->last = NULL;
}

OSErr DisposeTextBuffer(TextOutputBuffer *theBuffer) {
    TextBufferPtr temp;
    while (theBuffer->first != NULL) {
        temp = theBuffer->first;
        theBuffer->first = temp->next;
        DisposePtr((Ptr) temp);
    }
    InitTextBuffer(theBuffer);
    return noErr;
}

#define kTextBufferChunkSize (16*1024)

OSErr TextBufferWrite(TextOutputBuffer *theBuffer, void* data, long len) {
    unsigned char *src;
    long n, avail, count;
    TextBufferPtr storep;
    src = (unsigned char*) data;
    n = len;
    while (n > 0) {
            /* make sure there's a buffer */
        if (theBuffer->last == NULL) {
            storep = (TextBufferPtr) NewPtr(offsetof(TextBuffer, characters) + n + kTextBufferChunkSize);
            if (storep == NULL) return memFullErr;
            storep->next = NULL;
            storep->data.len = 0;
            storep->buffer.len = n + kTextBufferChunkSize;
            storep->data.strp = storep->buffer.strp = storep->characters;
            theBuffer->first = theBuffer->last = storep;
            avail = storep->buffer.len;
        }
            /* and there's some space in that buffer */
        storep = theBuffer->last;
        avail = storep->buffer.len - storep->data.len;
        if (avail == 0) {
            storep = (TextBufferPtr) NewPtr(offsetof(TextBuffer, characters) + n + kTextBufferChunkSize);
            if (storep == NULL) return memFullErr;
            storep->next = NULL;
            storep->data.len = 0;
            storep->buffer.len = n + kTextBufferChunkSize;
            storep->data.strp = storep->buffer.strp = storep->characters;
            theBuffer->last->next = storep;
            theBuffer->last = storep;
            avail = storep->buffer.len;
        }
            /* ceiling at available */
        count = ((n > avail) ? avail : n);
            /* copy bytes */
        BlockMoveData(src, storep->data.strp + storep->data.len, count);
            /* update pointers */
        src += count;
        storep->data.len += count;
        n -= count;
    }
    return noErr;
}

OSErr TextBufferSize(TextOutputBuffer *theBuffer, long *bytecount) {
    TextBufferPtr rover;
    long total;
    total = 0;
    for (rover = theBuffer->first; rover != NULL; rover = rover->next) {
        total += rover->data.len;
    }
    *bytecount = total;
    return noErr;

}

OSErr TextBufferLongTextString(TextOutputBuffer *theBuffer, LongTextStringPtr *theText) {
    TextBufferPtr rover;
    unsigned char *putp;
    long total;
    OSErr err;
    LongTextStringPtr theNewString;
    total = 0;
        /* calculate the length */
    for (rover = theBuffer->first; rover != NULL; rover = rover->next) {
        total += rover->data.len;
    }
        /* get a buffer */
    err = GetLongTextStringFromBuffer(NULL, total, &theNewString);
    if (err != noErr) return err;
        /* gather data */
    putp = theNewString->text.strp;
    for (rover = theBuffer->first; rover != NULL; rover = rover->next) {
        BlockMoveData(rover->data.strp, putp, rover->data.len);
        putp += rover->data.len;
    }
        /* done */  
    *theText = theNewString;
    return noErr;
}

OSErr TextBufferDataPtr(TextOutputBuffer *theBuffer, Ptr *theData) {
    TextBufferPtr rover;
    unsigned char *putp;
    long total;
    Ptr theNewData;
    total = 0;
        /* calculate the length */
    for (rover = theBuffer->first; rover != NULL; rover = rover->next) {
        total += rover->data.len;
    }
        /* get a buffer */
    theNewData = NewPtr(total);
    if (theNewData == NULL) return memFullErr;
        /* gather data */
    putp = (unsigned char*) theNewData;
    for (rover = theBuffer->first; rover != NULL; rover = rover->next) {
        BlockMoveData(rover->data.strp, putp, rover->data.len);
        putp += rover->data.len;
    }
        /* done */  
    *theData = theNewData;
    return noErr;
}

Boolean CopyTextBufferData(TextOutputBuffer *theBuffer, long offset, void* dstBuffer, long reqLength, long *actLength) {
    TextBufferPtr rover;
    unsigned char *putp, *getp, *endp;
    long local_offset, bytes_moved, to_move, move_avail, block_offset;

    local_offset = offset;
    bytes_moved = 0;
    block_offset = 0;
    putp = (unsigned char*) dstBuffer;

        /* copy bytes from offset */
    for (rover = theBuffer->first; rover != NULL; rover = rover->next) {
        if (local_offset >= block_offset && local_offset < block_offset + rover->data.len) {
            getp = rover->data.strp + (local_offset - block_offset);
            endp = rover->data.strp + rover->data.len;
            if ((getp < endp) && (bytes_moved < reqLength)) {
                to_move = reqLength - bytes_moved;
                move_avail = endp - getp;
                if (to_move > move_avail) to_move = move_avail;
                BlockMoveData(getp, putp, to_move);
                putp += to_move;
                getp += to_move;
                local_offset += to_move;
                bytes_moved += to_move;
            }
            if (bytes_moved == reqLength) break;
        }
        block_offset += rover->data.len;
    }
    if (actLength != NULL) *actLength = bytes_moved;
    return (bytes_moved == reqLength);
}




OSErr VSPrintfTextBuffer(TextOutputBuffer *theBuffer, const char *fmt, va_list args) {
    char const *pull;
    char *push, decb[32], *td, *end, localbuf[4096];
    unsigned char *rp;
    const char *syms = "0123456789ABCDEF";
    unsigned long value, i, n;
    long base, digits;
    Boolean twoscomp, hasDigits;
    LongTextStringPtr Lstring;
    TextReferencePtr textref;
    OSErr err;
    char state;
    Handle theHandle;


    push = localbuf;
    end = localbuf + sizeof(localbuf);
    pull = fmt;
    while (*pull) {
        if (*pull != '%') {
            if (push == end) {
                if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                push = localbuf;
            }
            *push++ = *pull++;
        } else {
            pull++; /* skip the % */
            if (*pull == '.') {
                pull++; /* skip the . */
                digits = 0;
                while (*pull >= '0' && *pull <= '9')
                    digits = (digits * 10) + ((*pull++) - '0');
                hasDigits = true;
            } else {
                digits = 0;
                hasDigits = false;
            }
            base = 0;
            switch(*pull) {
                case 'M':
                    pull++;  /* LongTextStringPtr/TextReferencePtr as html textref - skip the M */
                    Lstring = va_arg(args, LongTextStringPtr);
                        /* flush the local buffer */
                    if ((err = TextBufferWrite(theBuffer, localbuf, push - localbuf)) != noErr) goto bail;
                    push = localbuf;
                        /* write the html */
                    if ((err = EncodeHTMLTextStringProc(Lstring, false, theBuffer)) != noErr) goto bail;
                    break;
                case 'N':
                    pull++;  /* LongTextStringPtr/TextReferencePtr as html textref - skip the N */
                    Lstring = va_arg(args, LongTextStringPtr);
                        /* flush the local buffer */
                    if ((err = TextBufferWrite(theBuffer, localbuf, push - localbuf)) != noErr) goto bail;
                    push = localbuf;
                        /* write the html */
                    if ((err = EncodeHTMLTextStringProc(Lstring, true, theBuffer)) != noErr) goto bail;
                    break;

                case 'T':
                case 'L':
                    pull++;  /* LongTextStringPtr/TextReferencePtr textref - skip the T or L */
                    textref = va_arg(args, TextReferencePtr);
                    n = textref->len;
                    td = (char*) textref->strp; 
                    digits = 0;
                    for (i=0; i<n; i++) {
                        if (push == end) {
                            if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                            push = localbuf;
                        }
                        *push++ = *td++;
                    }
                    break;

                case 'H':
                    pull++;  /* Handle - skip the H */
                    theHandle = va_arg(args, Handle);
                    n = GetHandleSize(theHandle);
                    state = HGetState(theHandle);
                    HLock(theHandle);
                    td = (char*) (*theHandle); 
                    digits = 0;
                    for (i=0; i<n; i++) {
                        if (push == end) {
                            if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                            push = localbuf;
                        }
                        *push++ = *td++;
                    }
                    HSetState(theHandle, state);
                    break;
                case 's':
                    pull++;  /* skip the s */
                    td = va_arg(args, char*);
                    while (*td) {
                        if (push == end) {
                            if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                            push = localbuf;
                        }
                        *push++ = *td++;
                        digits--;
                        if (hasDigits && digits <= 0) break;
                    }
                    break;
                case 'p':
                    pull++;  /* skip the p */
                    rp = va_arg(args, unsigned char*);
                    for (i=0; i<*rp; i++) {
                        if (push == end) {
                            if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                            push = localbuf;
                        }
                        *push++ = (char) (rp[i+1]);
                        digits--;
                        if (hasDigits && digits <= 0) break;
                    }
                    break;
                case 'c':  /* skip the c */
                    pull++;
                    if (push == end) {
                        if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                        push = localbuf;
                    }
                    *push++ =  (char) (va_arg(args, long));
                    digits--;
                    break;
                case 'b': pull++; base = 2; twoscomp = false; break;
                case 'n': pull++; base = 4; twoscomp = false; break;
                case 'o': pull++; base = 8; twoscomp = false; break;
                case 'd': pull++; base = 10; twoscomp = true; break;
                case 'u': pull++; base = 10; twoscomp = false; break;
                case 'x': pull++; base = 16; twoscomp = false; break;
                default: digits = 0; base = 0; break;
            }
            if (base == 0) {
                while (digits > 0) {
                    if (push == end) {
                        if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                        push = localbuf;
                    }
                    *push++ = ' ';
                    digits--;
                }
            } else {
                value = va_arg(args, unsigned long);
                if (twoscomp && (value&0x80000000) != 0) {
                    if (push == end) {
                        if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                        push = localbuf;
                    }
                    *push++ = '-'; 
                    value = ((~value)+1);
                }
                td = decb;
                do {
                    *td++ = syms[value%base];
                    digits--;
                    value /= base;
                } while (value != 0);
                while (digits > 0) {
                    if (push == end) {
                        if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                        push = localbuf;
                    }
                    *push++ = '0';
                    digits--;
                }
                while (td != decb) {
                    if (push == end) {
                        if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) goto bail;
                        push = localbuf;
                    }
                    *push++ = *--td;
                }
            }
        }
    }
        /* flush the local buffer */
    if (push > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, push - localbuf)) != noErr) goto bail;
        push = localbuf;
    }
    return noErr;
bail:
    return err;
}





OSErr PrintfTextBuffer(TextOutputBuffer *theBuffer, const char *fmt, ...) {
    OSErr result;
    va_list args;
    va_start(args, fmt);
    result = VSPrintfTextBuffer(theBuffer, fmt, args);
    va_end(args);
    return result;
}










char* gHTMLRepCharTable[256] = {
    NULL, /* 000 - '' */
    NULL, /* 001 - '' */
    NULL, /* 002 - '' */
    NULL, /* 003 - '' */
    NULL, /* 004 - '' */
    NULL, /* 005 - '' */
    NULL, /* 006 - '' */
    NULL, /* 007 - '' */
    NULL, /* 008 - '' */
    NULL, /* 009 - '    ' */
    NULL, /* 010 - ' ' */
    NULL, /* 011 - ' ' */
    NULL, /* 012 - ' ' */
    NULL, /* 013 - ' ' */
    NULL, /* 014 - '' */
    NULL, /* 015 - '' */
    NULL, /* 016 - '' */
    NULL, /* 017 - '' */
    NULL, /* 018 - '' */
    NULL, /* 019 - '' */
    NULL, /* 020 - '' */
    NULL, /* 021 - '' */
    NULL, /* 022 - '' */
    NULL, /* 023 - '' */
    NULL, /* 024 - '' */
    NULL, /* 025 - '' */
    NULL, /* 026 - '' */
    NULL, /* 027 - '' */
    NULL, /* 028 - '' */
    NULL, /* 029 - '' */
    NULL, /* 030 - '' */
    NULL, /* 031 - '' */
    NULL, /* 032 - ' ' */
    NULL, /* 033 - '!' */
    "&quot;", /* 034 - '"' */
    NULL, /* 035 - '#' */
    NULL, /* 036 - '$' */
    NULL, /* 037 - '%' */
    "&amp;", /* 038 - '&' */
    NULL, /* 039 - ''' */
    NULL, /* 040 - '(' */
    NULL, /* 041 - ')' */
    NULL, /* 042 - '*' */
    NULL, /* 043 - '+' */
    NULL, /* 044 - ',' */
    NULL, /* 045 - '-' */
    NULL, /* 046 - '.' */
    NULL, /* 047 - '/' */
    NULL, /* 048 - '0' */
    NULL, /* 049 - '1' */
    NULL, /* 050 - '2' */
    NULL, /* 051 - '3' */
    NULL, /* 052 - '4' */
    NULL, /* 053 - '5' */
    NULL, /* 054 - '6' */
    NULL, /* 055 - '7' */
    NULL, /* 056 - '8' */
    NULL, /* 057 - '9' */
    NULL, /* 058 - ':' */
    NULL, /* 059 - ';' */
    "&lt;", /* 060 - '<' */
    NULL, /* 061 - '=' */
    "&gt;", /* 062 - '>' */
    NULL, /* 063 - '?' */
    NULL, /* 064 - '@' */
    NULL, /* 065 - 'A' */
    NULL, /* 066 - 'B' */
    NULL, /* 067 - 'C' */
    NULL, /* 068 - 'D' */
    NULL, /* 069 - 'E' */
    NULL, /* 070 - 'F' */
    NULL, /* 071 - 'G' */
    NULL, /* 072 - 'H' */
    NULL, /* 073 - 'I' */
    NULL, /* 074 - 'J' */
    NULL, /* 075 - 'K' */
    NULL, /* 076 - 'L' */
    NULL, /* 077 - 'M' */
    NULL, /* 078 - 'N' */
    NULL, /* 079 - 'O' */
    NULL, /* 080 - 'P' */
    NULL, /* 081 - 'Q' */
    NULL, /* 082 - 'R' */
    NULL, /* 083 - 'S' */
    NULL, /* 084 - 'T' */
    NULL, /* 085 - 'U' */
    NULL, /* 086 - 'V' */
    NULL, /* 087 - 'W' */
    NULL, /* 088 - 'X' */
    NULL, /* 089 - 'Y' */
    NULL, /* 090 - 'Z' */
    NULL, /* 091 - '[' */
    NULL, /* 092 - '\' */
    NULL, /* 093 - ']' */
    NULL, /* 094 - '^' */
    NULL, /* 095 - '_' */
    NULL, /* 096 - '`' */
    NULL, /* 097 - 'a' */
    NULL, /* 098 - 'b' */
    NULL, /* 099 - 'c' */
    NULL, /* 100 - 'd' */
    NULL, /* 101 - 'e' */
    NULL, /* 102 - 'f' */
    NULL, /* 103 - 'g' */
    NULL, /* 104 - 'h' */
    NULL, /* 105 - 'i' */
    NULL, /* 106 - 'j' */
    NULL, /* 107 - 'k' */
    NULL, /* 108 - 'l' */
    NULL, /* 109 - 'm' */
    NULL, /* 110 - 'n' */
    NULL, /* 111 - 'o' */
    NULL, /* 112 - 'p' */
    NULL, /* 113 - 'q' */
    NULL, /* 114 - 'r' */
    NULL, /* 115 - 's' */
    NULL, /* 116 - 't' */
    NULL, /* 117 - 'u' */
    NULL, /* 118 - 'v' */
    NULL, /* 119 - 'w' */
    NULL, /* 120 - 'x' */
    NULL, /* 121 - 'y' */
    NULL, /* 122 - 'z' */
    NULL, /* 123 - '{' */
    NULL, /* 124 - '|' */
    NULL, /* 125 - '}' */
    NULL, /* 126 - '~' */
    NULL, /* 127 - '' */
    "&Auml;", /* 128 - '' */
    "&Aring;", /* 129 - '' */
    "&Ccedil;", /* 130 - '' */
    "&Eacute;", /* 131 - '' */
    "&Ntilde;", /* 132 - '' */
```
| ```     "&Ouml;", /* 133 - '
' */ ``` |
```swift
    "&Uuml;", /* 134 - '' */
    "&aacute;", /* 135 - '' */
    "&agrave;", /* 136 - '' */
    "&acirc;", /* 137 - '' */
    "&auml;", /* 138 - '' */
    "&atilde;", /* 139 - '' */
    "&aring;", /* 140 - '' */
    "&ccedil;", /* 141 - '' */
    "&eacute;", /* 142 - '' */
    "&egrave;", /* 143 - '' */
    "&ecirc;", /* 144 - '' */
    "&euml;", /* 145 - '' */
    "&iacute;", /* 146 - '' */
    "&igrave;", /* 147 - '' */
    "&icirc;", /* 148 - '' */
    "&iuml;", /* 149 - '' */
    "&ntilde;", /* 150 - '' */
    "&oacute;", /* 151 - '' */
    "&ograve;", /* 152 - '' */
    "&ocirc;", /* 153 - '' */
    "&ouml;", /* 154 - '' */
    "&otilde;", /* 155 - '' */
    "&uacute;", /* 156 - '' */
    "&ugrave;", /* 157 - '' */
    "&ucirc;", /* 158 - '' */
    "&uuml;", /* 159 - '' */
    "&#134;", /* 160 - ' ' */
    "&deg;", /* 161 - '¡' */
    "&cent;", /* 162 - '¢' */
    "&pound;", /* 163 - '£' */
    "&sect;", /* 164 - '¤' */
    "&#149;", /* 165 - '¥' */
    "&para;", /* 166 - '¦' */
    NULL, /* 167 - '§' */
    "&reg;", /* 168 - '¨' */
    "&copy;", /* 169 - '©' */
    "&#153;", /* 170 - 'ª' */
    "&acute;", /* 171 - '«' */
    "&uml;", /* 172 - '¬' */
    NULL, /* 173 - '­' */
    "&AElig;", /* 174 - '®' */
    "&Oslash;", /* 175 - '¯' */
    NULL, /* 176 - '°' */
    "&plusmn;", /* 177 - '±' */
    NULL, /* 178 - '²' */
    NULL, /* 179 - '³' */
    "&yen;", /* 180 - '´' */
    "&micro;", /* 181 - 'µ' */
    NULL, /* 182 - '¶' */
    NULL, /* 183 - '·' */
    NULL, /* 184 - '¸' */
    NULL, /* 185 - '¹' */
    NULL, /* 186 - 'º' */
    "&ordf;", /* 187 - '»' */
    "&ordm;", /* 188 - '¼' */
    NULL, /* 189 - '½' */
    "&aelig;", /* 190 - '¾' */
    "&oslash;", /* 191 - '¿' */
    "&iquest;", /* 192 - 'À' */
    "&iexcl;", /* 193 - 'Á' */
    "&not;", /* 194 - 'Â' */
    NULL, /* 195 - 'Ã' */
    "&#131;", /* 196 - 'Ä' */
    NULL, /* 197 - 'Å' */
    NULL, /* 198 - 'Æ' */
    "&laquo;", /* 199 - 'Ç' */
    "&raquo;", /* 200 - 'È' */
    "&#133;", /* 201 - 'É' */
    "&nbsp;", /* 202 - 'Ê' */
    "&Agrave;", /* 203 - 'Ë' */
    "&Atilde;", /* 204 - 'Ì' */
    NULL, /* 205 - 'Í' */
    "&ETH;", /* 206 - 'Î' */
    NULL, /* 207 - 'Ï' */
    NULL, /* 208 - 'Ð' */
    "&#151;", /* 209 - 'Ñ' */
    "&#147;", /* 210 - 'Ò' */
    "&#148;", /* 211 - 'Ó' */
    "&#145;", /* 212 - 'Ô' */
    "&#146;", /* 213 - 'Õ' */
    "&divide;", /* 214 - 'Ö' */
    NULL, /* 215 - '×' */
    "&yuml;", /* 216 - 'Ø' */
    "&#159;", /* 217 - 'Ù' */
    NULL, /* 218 - 'Ú' */
    NULL, /* 219 - 'Û' */
    NULL, /* 220 - 'Ü' */
    NULL, /* 221 - 'Ý' */
    NULL, /* 222 - 'Þ' */
    NULL, /* 223 - 'ß' */
    "&#135;", /* 224 - 'à' */
    "&middot;", /* 225 - 'á' */
    "&#130;", /* 226 - 'â' */
    "&#132;", /* 227 - 'ã' */
    "&#137;", /* 228 - 'ä' */
    "&Acirc;", /* 229 - 'å' */
    "&Ecirc;", /* 230 - 'æ' */
    "&Aacute;", /* 231 - 'ç' */
    "&Euml;", /* 232 - 'è' */
    "&Egrave;", /* 233 - 'é' */
    "&Iacute;", /* 234 - 'ê' */
    "&Icirc;", /* 235 - 'ë' */
    "&Iuml;", /* 236 - 'ì' */
    "&Igrave;", /* 237 - 'í' */
    "&Oacute;", /* 238 - 'î' */
    "&Ocirc;", /* 239 - 'ï' */
    NULL, /* 240 - 'ð' */
    "&Ograve;", /* 241 - 'ñ' */
    "&Uacute;", /* 242 - 'ò' */
    "&Ucirc;", /* 243 - 'ó' */
    "&Ugrave;", /* 244 - 'ô' */
    NULL, /* 245 - 'õ' */
    "&#136;", /* 246 - 'ö' */
    NULL, /* 247 - '÷' */
    NULL, /* 248 - 'ø' */
    NULL, /* 249 - 'ù' */
    NULL, /* 250 - 'ú' */
    NULL, /* 251 - 'û' */
    NULL, /* 252 - 'ü' */
    NULL, /* 253 - 'ý' */
    NULL, /* 254 - 'þ' */
    NULL /* 255 - 'ÿ' */
};


OSErr EncodeHTMLTextStringProc(LongTextStringPtr textBuffer, Boolean addLineBreaks, TextOutputBuffer *theBuffer) {
    unsigned char *p, *q, *rep, reploc[2], localbuf[4096];
    OSErr err;
    long i;

        /* set up for run */
    if ( addLineBreaks )
        gHTMLRepCharTable['\r'] = gHTMLRepCharTable['\n'] = "<BR>\r";
    else gHTMLRepCharTable['\r'] = gHTMLRepCharTable['\n'] = NULL;
    if ( addLineBreaks )
        gHTMLRepCharTable[13] = "<BR>\r";
    else gHTMLRepCharTable[13] = NULL;

        /* translate bytes using the lookup table */
    q = localbuf;
    for (p = textBuffer->text.strp, i=0; i<textBuffer->text.len; i++, p++) {
            /* lookup replacement */
        if ((rep = (unsigned char*) gHTMLRepCharTable[*p]) == NULL) {
            reploc[0] = *p;
            reploc[1] = 0;
            rep = reploc;
        }
            /* store replacement in output */
        while (*rep) {
            if (q == (localbuf + sizeof(localbuf))) {
                err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf));
                if (err != noErr) goto bail;
                q = localbuf;
            }
            *q++ = *rep++;
        }
    }
        /* flush the buffer */
    if (q > localbuf) {
        err = TextBufferWrite(theBuffer, localbuf, (q - localbuf));
        if (err != noErr) goto bail;
    }
        /* done */
    return noErr;
bail:
    return err;
}

OSErr EncodeXMLTextStringProc(LongTextStringPtr textBuffer, TextOutputBuffer *theBuffer) {
    unsigned char *p, *q, *rep, reploc[2], localbuf[4096];
    OSErr err;
    long i;

        /* translate bytes using the lookup table */
    q = localbuf;
    for (p = textBuffer->text.strp, i=0; i<textBuffer->text.len; i++, p++) {
            /* calculate replacement sequence */
        switch (*p) {
            case '<': rep = "&lt;"; break;
            case '&': rep = "&amp;"; break;
            case '>': rep = "&gt;"; break;
            case '"': rep = "&quot;"; break;
            case '\'': rep = "&apos;"; break;
            default: reploc[0] = *p; reploc[1] = 0; rep = reploc; break;
        }
            /* store replacement in output */
        while (*rep) {
            if (q == (localbuf + sizeof(localbuf))) {
                err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf));
                if (err != noErr) goto bail;
                q = localbuf;
            }
            *q++ = *rep++;
        }
    }
        /* flush the buffer */
    if (q > localbuf) {
        err = TextBufferWrite(theBuffer, localbuf, (q - localbuf));
        if (err != noErr) goto bail;
    }
        /* done */
    return noErr;
bail:
    return err;
}




OSErr StripHTMLCommentsProc(LongTextStringPtr textBuffer, TextOutputBuffer *theBuffer) {
    unsigned char *p, *q, *start, localbuf[4096];
    OSErr err;
    long i, n;
    int state;

        /* translate bytes using the lookup table */
    q = localbuf;
    start = p = textBuffer->text.strp;
    state = 1;
    i = 0;
    n = textBuffer->text.len;
    while ( i < n ) {
        switch (state) {
            case 1:
                if ((n - i > 3) && p[0] == '<' && p[1] == '!' && p[2] == '-' && p[3] == '-') {
                    if (p[4] == '#') {
                        state = 3; /* pass through server side include directives */
                    } else {
                        state = 2;
                    }
                } else if ((n - i > 3) && p[0] == '-' && p[1] == '-' && p[2] == '>') {
                    return paramErr; /* nested comment */
                }
                break;
            case 3:
            case 2:
                if ((n - i >= 3) && p[0] == '-' && p[1] == '-' && p[2] == '>') {
                    if (state == 2) {
                        state = 1;
                        p += 3;
                        i += 3;
                        continue;
                    } else state = 1;
                } else if ((n - i > 3) && p[0] == '<' && p[1] == '!' && p[2] == '-' && p[3] == '-') {
                    return paramErr; /* nested comment */
                }
                break;
        }

            /* store replacement in output */
        if (i < n) {
            switch (state) {
                case 1:
                case 3:
                    if (q == (localbuf + sizeof(localbuf))) {
                        if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
                        q = localbuf;
                    }
                    *q++ = *p++;
                    i++;
                    break;
                case 2:
                    p++;
                    i++;
                    break;
            }
        }

    }
        /* check for unterminated comment */
    if (state == 2 || state == 3) {
        return paramErr;
    }
        /* flush the buffer */
    if (q > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, (q - localbuf))) != noErr) return err;
    }

        /* done */
    return noErr;
}









OSErr CountDelimitedSectionsProc(
                LongTextStringPtr textBuffer,
                LongTextStringPtr startPat, 
                LongTextStringPtr endPat, 
                Boolean caseSensitive, 
                long *count) {
    long startPos, endPos, total, position;
    Boolean searching;

        /* set up for run */
    total = position = 0;

        /* walk through the string counting instances */
    searching = true;
    while (searching) {
        if (FindLongTextString(textBuffer,  startPat->text.strp, startPat->text.len, position, caseSensitive, &startPos)) {
            if (FindLongTextString(textBuffer,  endPat->text.strp, endPat->text.len, startPos + startPat->text.len, caseSensitive, &endPos)) {
                total = total + 1;
                position = endPos + endPat->text.len;
            } else searching = false;
        } else searching = false;
    }
        /* save the count */
    *count = total;
    return noErr;
}




OSErr LocateAllDelimitedSectionsProc(
                TextReferencePtr textBuffer,
                TextReferencePtr startPat, 
                TextReferencePtr endPat, 
                Boolean caseSensitive, 
                long *count,
                TextReferencePtr *theSections) {

    OSErr err;
    TextReference nthSection;
    long startPos, endPos, startPatEnd, endPatEnd, position, total;
    Boolean searching;
    TextOutputBuffer theBuffer;
    TextReferencePtr theResult; 

        /* set up for run */
    InitTextBuffer(&theBuffer);
    theResult = NULL;

        /* walk through the string counting instances */
    searching = true;
    position = total = 0;
    while (searching) {
        if (SearchTextBuffer(textBuffer->strp, textBuffer->len,  startPat->strp, startPat->len, position, caseSensitive, &startPos)) {
            if (SearchTextBuffer(textBuffer->strp, textBuffer->len,  endPat->strp, endPat->len, startPos + startPat->len, caseSensitive, &endPos)) {
                    /* matched a section */
                position = endPos + endPat->len;
                    /* calculate pointers */
                startPatEnd = startPos + startPat->len;
                endPatEnd = endPos + endPat->len;
                    /* add the section to the list of sections */
                nthSection.strp = (textBuffer->strp + startPatEnd);
                nthSection.len = (endPos - startPatEnd);
                err = TextBufferWrite(&theBuffer, &nthSection, sizeof(nthSection));
                if (err != noErr) goto bail;
                total++;
            } else searching = false;
        } else searching = false;
    }
        /* save the resulting list */
    err = TextBufferDataPtr(&theBuffer, (Ptr*) &theResult);
    if (err != noErr) goto bail;
    DisposeTextBuffer(&theBuffer);
        /* save results */
    *count = total;
    *theSections = theResult;
        /* done */
    return noErr;
bail:
    DisposeTextBuffer(&theBuffer);
    return err;
}


OSErr GetAllDelimitedSectionsProc(
                LongTextStringPtr textBuffer,
                LongTextStringPtr startPat, 
                LongTextStringPtr endPat, 
                Boolean caseSensitive, 
                long *count,
                TextReferencePtr *theSections) {

    OSErr err;
    TextReference theTextBuffer, theStartPat, theEndPat;

    SetTextRefFromLongTextString(&theTextBuffer, textBuffer);
    SetTextRefFromLongTextString(&theStartPat, startPat);
    SetTextRefFromLongTextString(&theEndPat, endPat);

    err = LocateAllDelimitedSectionsProc( &theTextBuffer, &theStartPat, 
                &theEndPat, caseSensitive, count, theSections);

    return err;
}





OSErr LocateDelimitedSectionProc(
                TextReferencePtr textBuffer,
                TextReferencePtr startPat, 
                TextReferencePtr endPat, 
                Boolean caseSensitive,
                long sectionNumber,
                TextReference* sectionText, TextReference* outerBounds) {
    OSErr err;
    long startPos, endPos, startPatEnd, endPatEnd, total, position;
    Boolean searching, found;

        /* walk through the string counting instances */
    err = -10000;
    searching = true;
    found = false;
    total = position = 0;
    while (searching) {
        if (SearchTextBuffer(textBuffer->strp, textBuffer->len,  startPat->strp, startPat->len, position, caseSensitive, &startPos)) {
            if (SearchTextBuffer(textBuffer->strp, textBuffer->len,  endPat->strp, endPat->len, startPos + startPat->len, caseSensitive, &endPos)) {
                    /* found the section */
                total = total + 1;
                position = endPos + endPat->len;
                if (total == sectionNumber) {

                    startPatEnd = startPos + startPat->len;
                    endPatEnd = endPos + endPat->len;
                    if (sectionText != NULL) {
                        sectionText->strp = textBuffer->strp + startPatEnd;
                        sectionText->len = endPos - startPatEnd;
                    }
                    if (outerBounds != NULL) {
                        outerBounds->strp = textBuffer->strp + startPos;
                        outerBounds->len = endPos - startPos + endPat->len;
                    }
                    err = noErr;
                    found = true;
                    searching = false;
                }
            } else searching = false;
        } else searching = false;
    }
    if ( ! found ) err = -10000;
        /* done */
    return err;
}




/* GetDelimitedSection is an apple event handler called for 'open application' apple events. */
OSErr GetDelimitedSectionProc(
                LongTextStringPtr textBuffer,
                LongTextStringPtr startPat, 
                LongTextStringPtr endPat, 
                Boolean caseSensitive,
                long sectionNumber,
                LongTextStringPtr *sectionText) {
    OSErr err;
    TextReference theTextBuffer, theStartPat, theEndPat, theSectionText;

        /* walk through the string counting instances */
    SetTextRefFromLongTextString(&theTextBuffer, textBuffer);
    SetTextRefFromLongTextString(&theStartPat, startPat);
    SetTextRefFromLongTextString(&theEndPat, endPat);
    err = LocateDelimitedSectionProc( &theTextBuffer, &theStartPat, &theEndPat, caseSensitive, sectionNumber, &theSectionText, NULL);
    if (err == noErr)
        err = GetLongTextStringFromBuffer(theSectionText.strp, theSectionText.len, sectionText);
        /* done */
    return err;
}

OSErr SimpleGetDelimitedSection(
                LongTextStringPtr textBuffer,
                char* startingString, 
                char* endingString, 
                Boolean caseSensitive,
                long sectionNumber,
                LongTextStringPtr *sectionText) {
    TextReference theTextBuffer, theStartPat, theEndPat, theSectionText;
    OSErr err;
    SetTextRefFromLongTextString(&theTextBuffer, textBuffer);
    SetTextRefFromCString(&theStartPat, startingString);
    SetTextRefFromCString(&theEndPat, endingString);
    err = LocateDelimitedSectionProc( &theTextBuffer, &theStartPat, &theEndPat, caseSensitive, sectionNumber, &theSectionText, NULL);
    if (err == noErr)
        err = GetLongTextStringFromBuffer(theSectionText.strp, theSectionText.len, sectionText);
    return err;
}





OSErr ChangeDelimetedSection(
                TextReferencePtr textBuffer,
                TextReferencePtr startPat, 
                TextReferencePtr endPat, 
                TextReferencePtr newText, 
                Boolean caseSensitive,
                long sectionNumber,
                LongTextStringPtr *revisedText) {
    TextReference sectionText, partOne, partTwo;
    unsigned char *sectendp, *bufendp;
    unsigned long newLength;
    OSErr err;
    LongTextStringPtr textResult;

    err = LocateDelimitedSectionProc( textBuffer, startPat, endPat, caseSensitive, sectionNumber, &sectionText, NULL);
    if (err == noErr) {
        bufendp = textBuffer->strp + textBuffer->len;
        sectendp = sectionText.strp + sectionText.len;
        partOne.strp = textBuffer->strp;
        partOne.len = (sectionText.strp - textBuffer->strp);
        partTwo.strp = sectendp;
        partTwo.len = (bufendp - sectendp);
        if (newText == NULL) {
            newLength = (partOne.len + partTwo.len);
            err = GetLongTextStringFromBuffer(NULL, newLength, &textResult);
            if (err == noErr) {
                BlockMoveData(partOne.strp, textResult->text.strp, partOne.len);
                BlockMoveData(partTwo.strp, textResult->text.strp + partOne.len, partTwo.len);
                *revisedText = textResult;
            }
        } else {
            newLength = (partOne.len + newText->len + partTwo.len);
            err = GetLongTextStringFromBuffer(NULL, newLength, &textResult);
            if (err == noErr) {
                BlockMoveData(partOne.strp, textResult->text.strp, partOne.len);
                BlockMoveData(newText->strp, textResult->text.strp + partOne.len, newText->len);
                BlockMoveData(partTwo.strp, textResult->text.strp + partOne.len + newText->len, partTwo.len);
                *revisedText = textResult;
            }
        }           
    }
    return err;
}




OSErr SetDelimitedSectionProc(
                LongTextStringPtr textBuffer,
                LongTextStringPtr startPat, 
                LongTextStringPtr endPat, 
                LongTextStringPtr newText, 
                Boolean caseSensitive,
                long sectionNumber,
                LongTextStringPtr *revisedText) {

    TextReference theTextBuffer, theStartPat, theEndPat, theNewText;
    OSErr err;

    SetTextRefFromLongTextString(&theTextBuffer, textBuffer);
    SetTextRefFromLongTextString(&theStartPat, startPat);
    SetTextRefFromLongTextString(&theEndPat, endPat);
    if (newText == NULL) {
        err = ChangeDelimetedSection( &theTextBuffer, &theStartPat, &theEndPat, 
                    NULL, caseSensitive, sectionNumber, revisedText);
    } else {
        SetTextRefFromLongTextString(&theNewText, newText);
        err = ChangeDelimetedSection( &theTextBuffer, &theStartPat, &theEndPat, 
                    &theNewText, caseSensitive, sectionNumber, revisedText);
    }
    return err;
}


OSErr SimpleSetDelimitedSection(
                LongTextStringPtr textBuffer,
                char* startingString, 
                char* endingString, 
                LongTextStringPtr newText,
                Boolean caseSensitive,
                long sectionNumber,
                LongTextStringPtr *revisedText) {

    TextReference theTextBuffer, theStartPat, theEndPat, theNewText;
    OSErr err;

    SetTextRefFromLongTextString(&theTextBuffer, textBuffer);
    SetTextRefFromCString(&theStartPat, startingString);
    SetTextRefFromCString(&theEndPat, endingString);
    if (newText == NULL) {
        err = ChangeDelimetedSection( &theTextBuffer, &theStartPat, &theEndPat, 
                    NULL, caseSensitive, sectionNumber, revisedText);
    } else {
        SetTextRefFromLongTextString(&theNewText, newText);
        err = ChangeDelimetedSection( &theTextBuffer, &theStartPat, &theEndPat, 
                    &theNewText, caseSensitive, sectionNumber, revisedText);
    }
    return err;
}



OSErr DeleteDelimitedSectionProc(
                TextReferencePtr textBuffer,
                TextReferencePtr startPat, 
                TextReferencePtr endPat, 
                Boolean caseSensitive,
                long sectionNumber,
                LongTextStringPtr *revisedText) {

    TextReference completeSectionText, partOne, partTwo;
    unsigned char *sectendp, *bufendp;
    unsigned long newLength;
    LongTextStringPtr textResult;
    OSErr err;
    err = LocateDelimitedSectionProc( textBuffer, startPat, endPat, caseSensitive, sectionNumber, NULL, &completeSectionText);
    if (err == noErr) {
        bufendp = textBuffer->strp + textBuffer->len;
        sectendp = completeSectionText.strp + completeSectionText.len;
        partOne.strp = textBuffer->strp;
        partOne.len = (completeSectionText.strp - textBuffer->strp);
        partTwo.strp = sectendp;
        partTwo.len = (bufendp - sectendp);
        newLength = (partOne.len + partTwo.len);
        err = GetLongTextStringFromBuffer(NULL, newLength, &textResult);
        if (err == noErr) {
            BlockMoveData(partOne.strp, textResult->text.strp, partOne.len);
            BlockMoveData(partTwo.strp, textResult->text.strp + partOne.len, partTwo.len);
            *revisedText = textResult;
        }
    }
    return err;
}

OSErr RemoveDelimitedSectionProc(
                LongTextStringPtr textBuffer,
                LongTextStringPtr startPat, 
                LongTextStringPtr endPat, 
                Boolean caseSensitive,
                long sectionNumber,
                LongTextStringPtr *revisedText) {

    TextReference theTextBuffer, theStartPat, theEndPat;
    OSErr err;

    SetTextRefFromLongTextString(&theTextBuffer, textBuffer);
    SetTextRefFromLongTextString(&theStartPat, startPat);
    SetTextRefFromLongTextString(&theEndPat, endPat);
    err = DeleteDelimitedSectionProc( &theTextBuffer, &theStartPat, &theEndPat, 
                caseSensitive, sectionNumber, revisedText);
    return err;
}












OSErr DecodeCGIStringToBuffer(unsigned char* buffer, long length, TextOutputBuffer *theBuffer) {
    char* hexChars = "0123456789ABCDEF", *hexp;
    unsigned char *src, *dst, *end, localbuf[2048];
    OSErr err;

        /* translate bytes using the lookup table */
    dst = localbuf;
    src = buffer;
    end = buffer + length;
    while (src < end) {
            /* make sure there's room for at least one character */
        if (dst == (localbuf + sizeof(localbuf))) {
            if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
            dst = localbuf;
        }
            /* stash the character */
        if (*src == '+') {
            *dst++ = ' ';
            src++;
        } else if (*src == '%') {
                /* verify length */
            if (end - src < 3) return paramErr;
                /* the first digit */
            hexp = strchr(hexChars, (char) gUpcaseTable[src[1]]);
            if (hexp == NULL) return paramErr;
            *dst = (hexp - hexChars) << 4;
                /* the second digit */
            hexp = strchr(hexChars, (char) gUpcaseTable[src[2]]);
            if (hexp == NULL) return paramErr;
            *dst |= (hexp - hexChars);
                /* move to next */
            src += 3;
            dst++;
        } else {
            *dst++ = *src++;
        }
    }
        /* flush the buffer */
    if (dst > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, (dst - localbuf))) != noErr) return err;
    }
        /* done */
    return noErr;
}

LongTextStringPtr DecodeCGIStringToString(unsigned char* buffer, long length) {
    TextOutputBuffer theBuffer;
    LongTextStringPtr theResult;
    OSErr err;
        /* initial state */
    InitTextBuffer(&theBuffer);
    theResult = NULL;
        /* write to the buffer */
    err = DecodeCGIStringToBuffer(buffer, length, &theBuffer);
    if (err == noErr) {
            /* save the string */
        err = TextBufferLongTextString(&theBuffer, &theResult);
        if (err != noErr) theResult = NULL;
    }
        /* release the buffer */
    DisposeTextBuffer(&theBuffer);
    return theResult;
}

OSErr EncodeStringToCGIBuffer(unsigned char* buffer, long length, Boolean specialSpaces, TextOutputBuffer *theBuffer) {
    char* hexChars = "0123456789ABCDEF";
    unsigned char *src, *dst, *end, localbuf[2048];
    OSErr err;
        /* translate bytes using the lookup table */
    dst = localbuf;
    src = buffer;
    end = buffer + length;
    while (src < end) {
            /* make sure there's room for at least three characters */
        if ((dst - localbuf) > (sizeof(localbuf) - 3)) {
            if ((err = TextBufferWrite(theBuffer, localbuf, dst - localbuf)) != noErr) return err;
            dst = localbuf;
        }
            /* stash the character */
        if (specialSpaces && (*src == ' ')) {
            *dst++ = '+';
            src++;
        } else if ((*src >= 'a' && *src <= 'z') || (*src >= 'A' && *src <= 'Z') || (*src >= '0' && *src <= '9')) {
            *dst++ = *src++;
        } else {
            *dst++ = '%';
            *dst++ = hexChars[((*src >> 4) & 15)];
            *dst++ = hexChars[(*src & 15)];
            src++;
        }
    }
        /* flush the buffer */
    if (dst > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, dst - localbuf)) != noErr) return err;
    }
    return noErr;
}

LongTextStringPtr EncodeStringToCGIString(unsigned char* buffer, long length, Boolean specialSpaces) {
    TextOutputBuffer theBuffer;
    LongTextStringPtr theResult;
    OSErr err;
        /* initial state */
    InitTextBuffer(&theBuffer);
    theResult = NULL;
        /* write to the buffer */
    err = EncodeStringToCGIBuffer(buffer, length, specialSpaces, &theBuffer);
    if (err == noErr) {
            /* save the string */
        err = TextBufferLongTextString(&theBuffer, &theResult);
        if (err != noErr) theResult = NULL;
    }
        /* release the buffer */
    DisposeTextBuffer(&theBuffer);
    return theResult;
}





OSErr AccumulateFormLetter(
                TextOutputBuffer *theBuffer,
                TextReferencePtr textBuffer,
                FormLetterElementTable repsTable, 
                long repsTableLength, 
                Boolean caseSensitive ) {

    FormLetterElement *repElt;  
    Boolean found;
    long i, j, n, cmpVal;
    unsigned char *p, *src, *dst, *end, localbuf[4096];
    OSErr err;

        /* translate bytes using the lookup table */
    dst = localbuf;
    p = textBuffer->strp;
    end = p + textBuffer->len;
    while (p < end) {
        found = false;
            /* lookup replacement */
        for (repElt = repsTable, j=0; j< repsTableLength; j++, repElt++) {
            if ((p+repElt->pattext.len) <= end) {
                cmpVal = CompareTextBuffers( repElt->pattext.strp, repElt->pattext.len, p, repElt->pattext.len, caseSensitive);
                if (cmpVal == 0) {
                    p += repElt->pattext.len;
                    n = repElt->reptext.len;
                    src = (unsigned char*) repElt->reptext.strp;
                    for (i=0; i<n;i++) {
                        if (dst == (localbuf + sizeof(localbuf))) {
                            if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
                            dst = localbuf;
                        }
                        *dst++ = *src++;
                    }
                    found = true;
                    break;
                }
            }
        }
        if ( ! found ) {
            if (dst == (localbuf + sizeof(localbuf))) {
                if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
                dst = localbuf;
            }
            *dst++ = *p++;
        }
    }
        /* flush the buffer */
    if (dst > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, (dst - localbuf))) != noErr) return err;
    }
        /* done */
    return noErr;
}




OSErr FillFormLetter(
                TextReferencePtr textBuffer,
                FormLetterElementTable repsTable, 
                long repsTableLength, 
                Boolean caseSensitive,
                LongTextStringPtr *revistedText) {

    TextOutputBuffer theBuffer;
    OSErr err;
    LongTextStringPtr localResult;

        /* set up for run */
    InitTextBuffer(&theBuffer);

    err = AccumulateFormLetter( &theBuffer, textBuffer, repsTable, repsTableLength, caseSensitive );
    if (err == noErr) {
        err = TextBufferLongTextString(&theBuffer, &localResult);
        if (err == noErr) {
            *revistedText = localResult;
        }
    }
    DisposeTextBuffer(&theBuffer);
    return err;
}



OSErr FormLetterReplacementProc(
                LongTextStringPtr textBuffer,
                FormLetterElementTable repsTable, 
                long repsTableLength, 
                Boolean caseSensitive,
                LongTextStringPtr *revistedText) {
    OSErr err;
    TextReference templateBuffer;
    SetTextRefFromLongTextString(&templateBuffer, textBuffer);
    err = FillFormLetter(&templateBuffer, repsTable,  repsTableLength, caseSensitive, revistedText);
    return err;
}





typedef struct {
    char* pattern;
    int len;
    unsigned char ch;
} HTMLEntityTupple;

HTMLEntityTupple gHTMLPatTable[] = {
    { "&gt;", 4, '>' },
    { "&lt;", 4, '<' },
    { "&nbsp;", 6, 'Ê' },
    { "&amp;", 5, '&' },
    { "&quot;", 6, '"' },
    { "&iexcl;", 7, 'Á' },
    { "&cent;", 6, '¢' },
    { "&pound;", 7, '£' },
    { "&yen;", 5, '´' },
    { "&sect;", 6, '¤' },
    { "&copy;", 6, '©' },
    { "&laquo;", 7, 'Ç' },
    { "&raquo;", 7, 'È' },
    { "&not;", 5, 'Â' },
    { "&reg;", 5, '¨' },
    { "&deg;", 5, '¡' },
    { "&plusmn;", 8, '±' },
    { "&uml;", 5, '¬' },
    { "&acute;", 7, '«' },
    { "&micro;", 7, 'µ' },
    { "&para;", 6, '¦' },
    { "&middot;", 8, 'á' },
    { "&iquest;", 8, 'À' },
    { "&ordm;", 6, '¼' },
    { "&ordf;", 6, '»' },
    { "&#130;", 6, 'â' },
    { "&#131;", 6, 'Ä' },
    { "&#132;", 6, 'ã' },
    { "&#133;", 6, 'É' },
    { "&#134;", 6, ' ' },
    { "&#135;", 6, 'à' },
    { "&#136;", 6, 'ö' },
    { "&#137;", 6, 'ä' },
    { "&#145;", 6, 'Ô' },
    { "&#146;", 6, 'Õ' },
    { "&#147;", 6, 'Ò' },
    { "&#148;", 6, 'Ó' },
    { "&#149;", 6, '¥' },
    { "&#151;", 6, 'Ñ' },
    { "&#153;", 6, 'ª' },
    { "&#159;", 6, 'Ù' },
    { "&Agrave;", 8, 'Ë' },
    { "&Aacute;", 8, 'ç' },
    { "&Acirc;", 7, 'å' },
    { "&Atilde;", 8, 'Ì' },
    { "&Auml;", 6, '' },
    { "&Aring;", 7, '' },
    { "&AElig;", 7, '®' },
    { "&Ccedil;", 8, '' },
    { "&Egrave;", 8, 'é' },
    { "&Eacute;", 8, '' },
    { "&Ecirc;", 7, 'æ' },
    { "&Euml;", 6, 'è' },
    { "&Igrave;", 8, 'í' },
    { "&Iacute;", 8, 'ê' },
    { "&Icirc;", 7, 'ë' },
    { "&Iuml;", 6, 'ì' },
    { "&ETH;", 5, 'Î' },
    { "&Ntilde;", 8, '' },
    { "&Ograve;", 8, 'ñ' },
    { "&Oacute;", 8, 'î' },
    { "&Ocirc;", 7, 'ï' },
```
| ```     { "&Ouml;", 6, '
' }, ``` |
```swift
    { "&Oslash;", 8, '¯' },
    { "&Ugrave;", 8, 'ô' },
    { "&Uacute;", 8, 'ò' },
    { "&Ucirc;", 7, 'ó' },
    { "&Uuml;", 6, '' },
    { "&agrave;", 8, '' },
    { "&aacute;", 8, '' },
    { "&acirc;", 7, '' },
    { "&atilde;", 8, '' },
    { "&auml;", 6, '' },
    { "&aring;", 7, '' },
    { "&aelig;", 7, '¾' },
    { "&ccedil;", 8, '' },
    { "&egrave;", 8, '' },
    { "&eacute;", 8, '' },
    { "&ecirc;", 7, '' },
    { "&euml;", 6, '' },
    { "&igrave;", 8, '' },
    { "&iacute;", 8, '' },
    { "&icirc;", 7, '' },
    { "&iuml;", 6, '' },
    { "&ntilde;", 8, '' },
    { "&otilde;", 8, '' },
    { "&ograve;", 8, '' },
    { "&oacute;", 8, '' },
    { "&ocirc;", 7, '' },
    { "&ouml;", 6, '' },
    { "&divide;", 8, 'Ö' },
    { "&oslash;", 8, '¿' },
    { "&ugrave;", 8, '' },
    { "&uacute;", 8, '' },
    { "&ucirc;", 7, '' },
    { "&uuml;", 6, '' },
    { "&yuml;", 6, 'Ø' }
};
#define kNumHTMLPatterns (sizeof(gHTMLPatTable)/sizeof(HTMLEntityTupple))




OSErr DecodeHTMLStringToBuffer(unsigned char* buffer, long length, TextOutputBuffer *theBuffer) {
    unsigned char *p, *q, *rep, reploc[4], localbuf[4096];
    long j;
    OSErr err;

        /* translate bytes using the lookup table */
    q = localbuf;
    p = buffer;
    while ((p - buffer) < length) {
        if (*p == '<') { /* <BR>'s to returns */
            if ((((p+3) - buffer) < length)
            && ((p[1] == 'B') || (p[1] == 'b')) 
            && ((p[2] == 'R') || (p[2] == 'r')) 
            && (p[3] == '>')) {
                reploc[0] = '\r';
                p += 4;
            } else { /* skip everything else */
                while ((p - buffer) < length) {
                    if (*p++ == '>') break;
                }
                continue;
            }
        } else if (*p == '&') {

            if (p[1] == '#') { /* &#nnn; */
                if ( (((p+6) - buffer) <= length)
                && (p[2] >= '0' && p[2] <= '9')
                && (p[3] >= '0' && p[3] <= '9')
                && (p[4] >= '0' && p[4] <= '9')
                && p[5] == ';' ) {
                    j = (p[2] - '0') * 100 + (p[3] - '0') * 10 + (p[4] - '0');
                    if (j > 255) {
                        return paramErr; /* out of range */
                    }
                    reploc[0] = (unsigned char) j;
                    p += 6;
                } else {
                    return paramErr; /* wrong format */
                }
            } else {
                HTMLEntityTupple *nthPat;
                for (nthPat=gHTMLPatTable, j=0; j<kNumHTMLPatterns; j++,nthPat++)
                    if ((((p+nthPat->len) - buffer) <= length)
                    && (strncmp((char*) p, nthPat->pattern, nthPat->len) == 0))
                        break;
                if (j<kNumHTMLPatterns) {
                    reploc[0] = nthPat->ch;
                    p += nthPat->len;
                } else {
                    return paramErr;
                }
            }
        } else {
            reploc[0] = *p++;
        }
        reploc[1] = 0;
        rep = reploc;
            /* store replacement in output */
        while (*rep) {
            if (q == (localbuf + sizeof(localbuf))) {
                if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
                q = localbuf;
            }
            *q++ = *rep++;
        }
    }
        /* flush the buffer */
    if (q > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, (q - localbuf))) != noErr) return err;
    }
    return noErr;
}


HTMLEntityTupple gXMLPatTable[] = {
    { "&gt;", 4, '>' },
    { "&amp;", 5, '&' },
    { "&lt;", 4, '<' },
    { "&quot;", 6, '"' },
    { "&apos;", 6, '\'' }
};

#define kNumXMLPatterns (sizeof(gXMLPatTable)/sizeof(HTMLEntityTupple))

OSErr DecodeXMLStringToBuffer(unsigned char* buffer, long length, TextOutputBuffer *theBuffer) {
    unsigned char *p, *q, *rep, reploc[4], localbuf[4096];
    long j;
    OSErr err;

        /* translate bytes using the lookup table */
    q = localbuf;
    p = buffer;
    while ((p - buffer) < length) {
        if (*p == '&') {

            HTMLEntityTupple *nthPat;
            for (nthPat=gXMLPatTable, j=0; j<kNumXMLPatterns; j++,nthPat++)
                if ((((p+nthPat->len) - buffer) <= length)
                && (strncmp((char*) p, nthPat->pattern, nthPat->len) == 0))
                    break;
            if (j<kNumXMLPatterns) {
                reploc[0] = nthPat->ch;
                p += nthPat->len;
            } else {
                return paramErr;
            }
        } else {
            reploc[0] = *p++;
        }
        reploc[1] = 0;
        rep = reploc;
            /* store replacement in output */
        while (*rep) {
            if (q == (localbuf + sizeof(localbuf))) {
                if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
                q = localbuf;
            }
            *q++ = *rep++;
        }
    }
        /* flush the buffer */
    if (q > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, (q - localbuf))) != noErr) return err;
    }
    return noErr;
}



LongTextStringPtr DecodeHTMLString(unsigned char* buffer, long length) {
    TextOutputBuffer theBuffer;
    LongTextStringPtr theResult;
    OSErr err;
        /* initial state */
    InitTextBuffer(&theBuffer);
    theResult = NULL;
        /* write to the buffer */
    err = DecodeHTMLStringToBuffer(buffer, length, &theBuffer);
    if (err == noErr) {
            /* save the string */
        err = TextBufferLongTextString(&theBuffer, &theResult);
        if (err != noErr) theResult = NULL;
    }
        /* release the buffer */
    DisposeTextBuffer(&theBuffer);
    return theResult;
}


/* OpenApplication is an apple event handler called for 'open application' apple events. */
OSErr EncodeTextAsURLTextToBuffer(unsigned char* buffer, long length, TextOutputBuffer *theBuffer) {
    char* validChars = "$-.+!*'()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    char* hexChars = "0123456789ABCDEF";
    long i;
    unsigned char *p, *k, *q, *rep, reploc[4], localbuf[4096];
    OSErr err;
        /* translate bytes using the lookup table */
    q = localbuf;
    for (p = buffer, i=0; i<length; i++, p++) {
            /* if it's an 'okay' character, just stick it in... */
        for (k = (unsigned char*)validChars; *k; k++) {
            if (*p == *k) break;
        }
        if (*k != 0) {
            reploc[0] = *p;
            reploc[1] = 0;
        } else {
            reploc[0] = '%';
            reploc[1] = (unsigned char) hexChars[((*p)>>4) & 15];
            reploc[2] = (unsigned char) hexChars[(*p) & 15];
            reploc[3] = 0;
        }
        rep = reploc;
            /* store replacement in output */
        while (*rep) {
            if (q == (localbuf + sizeof(localbuf))) {
                if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
                q = localbuf;
            }
            *q++ = *rep++;
        }
    }
        /* flush the buffer */
    if (q > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, (q - localbuf))) != noErr) return err;
    }
    return noErr;
}


LongTextStringPtr EncodeTextAsURLTextToString(unsigned char* buffer, long length) {
    TextOutputBuffer theBuffer;
    LongTextStringPtr theResult;
    OSErr err;
        /* initial state */
    InitTextBuffer(&theBuffer);
    theResult = NULL;
        /* write to the buffer */
    err = EncodeTextAsURLTextToBuffer(buffer, length, &theBuffer);
    if (err == noErr) {
            /* save the string */
        err = TextBufferLongTextString(&theBuffer, &theResult);
        if (err != noErr) theResult = NULL;
    }
        /* release the buffer */
    DisposeTextBuffer(&theBuffer);
    return theResult;
}


OSErr DecodeURLTextAsTextToBuffer(unsigned char* buffer, long length, TextOutputBuffer *theBuffer) {
    char* hexChars = "0123456789ABCDEF", *hexp;
    unsigned char *p, *q, *rep, reploc[4], localbuf[4096];
    OSErr err;

        /* translate bytes using the lookup table */
    q = localbuf;
    p = buffer;
    while ((p - buffer) < length) {
        if (*p == '%') {
            if (((p+2) - buffer) >= length
                || p[1] == 0
                || p[2] == 0) return paramErr;
                /* the first digit */
            hexp = strchr(hexChars, gUpcaseTable[p[1]]);
            if (hexp == NULL) return paramErr;
            reploc[0] = (hexp - hexChars) << 4;
                /* the second digit */
            hexp = strchr(hexChars, gUpcaseTable[p[2]]);
            if (hexp == NULL) return paramErr;
            reploc[0] |= (hexp - hexChars);
            p += 3;
        } else {
            reploc[0] = *p++;
        }
        reploc[1] = 0;
        rep = reploc;
            /* store replacement in output */
        while (*rep) {
            if (q == (localbuf + sizeof(localbuf))) {
                if ((err = TextBufferWrite(theBuffer, localbuf, sizeof(localbuf))) != noErr) return err;
                q = localbuf;
            }
            *q++ = *rep++;
        }
    }
        /* flush the buffer */
    if (q > localbuf) {
        if ((err = TextBufferWrite(theBuffer, localbuf, (q - localbuf))) != noErr) return err;
    }

    return noErr;
}


LongTextStringPtr DecodeURLTextAsTextToString(unsigned char* buffer, long length) {
    TextOutputBuffer theBuffer;
    LongTextStringPtr theResult;
    OSErr err;
        /* initial state */
    InitTextBuffer(&theBuffer);
    theResult = NULL;
        /* write to the buffer */
    err = DecodeURLTextAsTextToBuffer(buffer, length, &theBuffer);
    if (err == noErr) {
            /* save the string */
        err = TextBufferLongTextString(&theBuffer, &theResult);
        if (err != noErr) theResult = NULL;
    }
        /* release the buffer */
    DisposeTextBuffer(&theBuffer);
    return theResult;
}
```

[Next](TextUtilities.h.md)[Previous](PixOps.h.md)

