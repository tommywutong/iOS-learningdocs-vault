---
title: enetlognke
apple_id: DTS10003579
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2014-05-12'
source_url: https://developer.apple.com/library/archive/samplecode/enetlognke/Listings/enetlognke_c.html
archived_at: '2026-07-18T03:29:09.018727Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [enetlognke](enetlognke.md)


[Next](Read%20Me.txt.md)[Previous](enetlognke.md)

# enetlognke.c

```c
/*
     File: enetlognke.c
 Abstract: A simple interface filter NKE.
  Version: 2.0

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

// Have to disable the sign conversion warning around this include because of a bug 
// in the header <rdar://problem/16324663>.

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wsign-conversion"

#include <libkern/libkern.h>

#pragma clang diagnostic pop

#include <sys/lock.h>
#include <mach/vm_types.h>
#include <mach/kmod.h>
#include <sys/socket.h>
#include <sys/kpi_mbuf.h>
#include <net/kpi_interface.h>
#include <net/kpi_interfacefilter.h>
#include <sys/syslog.h>
#include <libkern/OSMalloc.h>
#include <sys/kernel.h>
#include <sys/systm.h>
#include <netinet/in.h>
#include <kern/locks.h>
#include <sys/kern_event.h>
#include <stdarg.h>
#include <pexpert/pexpert.h>
#include <kern/assert.h>
#include <libkern/OSAtomic.h>

#pragma mark * Configurable Parameters

// The bundle ID of this kernel extension.  We can't make this a static variable 
// because it's used as part of the initialisation of gInterfaceFilterInfo structure.

#define MYBUNDLEID  "com.example.apple-samplecode.kext.enetlognke"

/*! The interface to filter.  The default value, "en0", is typically the first 
 *  built-in Ethernet-like interface (the built-in Wi-Fi on modern machines, 
 *  the built-in Ethernet on older machines).  You must change this if you want 
 *  to test with some other interface.
 */
// 

static const char * gNameOfInterfaceToFilter = "en0";

enum {
    kSwallowPackets = FALSE             ///< Controls whether the code just filters (FALSE) or demos packet swallow / re-injection (TRUE).
};

enum {
    kLogPacketByteCount = 18            ///< If non-zero, the filter logs the first N bytes of each packet.
};

#pragma mark Utility Functions

/*! Converts a protocol number to a user-visible name string.
 *  \param protocol The protocol number.
 *  \param str A buffer into which to store the string.
 *  \param strSize The size of that buffer.
 */

static void 
ProtocolToString(protocol_family_t protocol, char str[], size_t strSize)
{
    assert(str != NULL);
    assert(strSize != 0);
    switch (protocol) {
        case AF_UNSPEC:     strlcpy(str, "UNSP", strSize); break;
        case AF_INET:       strlcpy(str, "IPv4", strSize); break;
        case AF_INET6:      strlcpy(str, "IPv6", strSize); break;
        default:            snprintf(str, strSize, "%3u?", (unsigned int) protocol); break;
    }
}

/*! Prints the first kLogPacketByteCount bytes of an Ethernet-like packet within an mbuf.
 *  \param frame A pointer to frame data to be printed before the mbuf data, or NULL.
 *  \param frameSize The length of any frame data, or 0.
 *  \param m The mbuf containing the packet to print.
 */

static void 
PrintPacketHeader(const void * frame, size_t frameSize, mbuf_t m)
{
    const uint8_t * data;
    size_t          dataLength;
    size_t          dataIndex;
    mbuf_t          mNext;
    size_t          bytesLeftToPrint;
    size_t          column;

    assert(kLogPacketByteCount != 0);               // Shouldn't be called unless logging is enabled.
    // frame may be NULL
    assert( (frameSize != 0) || (frame == NULL) );
    assert(m != NULL);

    // If we've got no leading frame, start with the mbuf.
    // Otherwise we start with the frame.

    if (frame == NULL) {
        data       = mbuf_data(m);
        dataLength = mbuf_len(m);
        mNext      = mbuf_next(m);
    } else {
        data       = frame;
        dataLength = frameSize;
        mNext      = m;
    }

    // Looping printing data.

    bytesLeftToPrint = kLogPacketByteCount;
    column = 0;
    do {
        size_t          bytesToPrintNow;

        // Print the current chunk of data (but no more than bytesLeftToPrint).

        bytesToPrintNow = dataLength;
        if (bytesToPrintNow > bytesLeftToPrint) {
            bytesToPrintNow = bytesLeftToPrint;
        }
        for (dataIndex = 0; dataIndex < bytesToPrintNow; dataIndex++, column++) {
            printf("%02x", data[dataIndex]);
            if (column == 5 ) printf("|");         // print '|' after the destination address
            if (column == 11) printf("|");         // print '|' after the source address
            if (column == 13) printf("|");         // print '|' after the protocol/length field
        }

        // Stop if we don't need to print any more.

        bytesLeftToPrint -= bytesToPrintNow;
        if (bytesLeftToPrint == 0) {
            break;
        }

        // Stop if there is no next mbuf to work on.

        if (mNext == NULL) {
            break;
        }

        // Otherwise move on to the next mbuf.

        data       = mbuf_data(mNext);
        dataLength = mbuf_len(mNext);
        mNext      = mbuf_next(mNext);
    } while (TRUE);
}

/*! Prints a summary of a packet running through the filter.
 *  \param caller Identifiers the caller (and hence whether it's an input or output packet).
 *  \param protocol The protocol number for this packet.
 *  \param m The mbuf containing the packet to print.
 */

static void 
PrintPacketSummary(const char * caller, protocol_family_t protocol, const void * frame, size_t frameSize, mbuf_t m, boolean_t isDuplicate)
{
    mbuf_t      cursor;
    char        protocolName[16];
    size_t      packetByteCount;

    assert(kLogPacketByteCount != 0);               // Shouldn't be called unless logging is enabled.
    assert(caller != NULL);
    assert(m != NULL);

    ProtocolToString(protocol, protocolName, sizeof(protocolName));

    cursor = m;
    packetByteCount = frameSize;
    do {
        packetByteCount += mbuf_len(m);
        cursor = mbuf_next(cursor);
    } while (cursor != NULL);

    printf("enetlognke %s %s ", caller, protocolName);
    PrintPacketHeader(frame, frameSize, m);
    printf(" %4lu%s\n", (unsigned long) packetByteCount, isDuplicate ? " +" : "");
}

#pragma mark * Memory Subsystem

/*! A malloc tag used by the OSMalloc calls to associated our memory allocations 
 *  with this KEXT.  This is the preferred memory allocation method for KEXTs 
 *  (replacing MALLOC and FREE).
 */

static OSMallocTag  gOSMallocTag;

/*! Sets up memory management by creating a malloc tag.
 *  \param name The name for the malloc tag.
 */

static boolean_t 
StartMemorySubsystem(const char * name)
{
    boolean_t       success;

    assert(name != NULL);

    success = TRUE;

    gOSMallocTag = OSMalloc_Tagalloc(name, OSMT_DEFAULT);
    if (gOSMallocTag == NULL) {
        printf("enetlognke err OSMalloc_Tagalloc\n");
        success = FALSE;
    }

    return success;
}

/*! Cleans up memory management by freeing the malloc tag.
 */

static void 
StopMemorySubsystem(void)
{
    if (gOSMallocTag != NULL) {
        OSMalloc_Tagfree(gOSMallocTag);
        gOSMallocTag = NULL;
    }
}

#pragma mark * MBuf Tag Subsystem

/*  This KEXT uses tags to mark which packets it has previously processed.  This is most important 
    when swallowing/re-injecting packets but it's a good idea to mark packets like this always because 
    another interface filter could re-inject a packet and your filter will then be called to process the 
    same packet again.
*/

static mbuf_tag_id_t        gMyMBufTagID;   ///< An mbuf tag ID namespace for our KEXT.

enum {
    kMyMBufTagTypeFlags = 1                 ///< Identifies our flags mbuf tag within the gMyMBufTagID namespace;.
};

/*! Defines a set of flags that we stored in an mbuf tag to track the state of our processing of a packet. 
 */

typedef unsigned int MyMBufTagFlags;
enum MyMBufTagFlags {
    kMyMBufTagFlagsInputDone  = 1U << 0,    ///< Set if packet has been processed by our input filter.
    kMyMBufTagFlagsOutputDone = 1U << 1     ///< Set if packet has been processed by our output filter.
};

/*! Starts the mbuf tag subsystem.
 *  \returns TRUE if the subsystem was successfully started.
 */

static boolean_t 
StartMBufTagSubsystem(const char * moduleName)
{
    errno_t     err;

    assert(moduleName != NULL);

    err = mbuf_tag_id_find(moduleName, &gMyMBufTagID);
    if (err != 0) {
        printf("enetlognke err mbuf_tag_id_find -> %d\n", err);
    }
    return err == 0;
}

// Note: There is no StopMBufTagSubsystem because mbuf tag IDs can't be deallocated.

/*! Tests whether a particular flag has been set in our mbuf tag.
 *  \param m The mbuf whose tags we are checking.
 *  \param flag The flag to check.
 *  \returns TRUE if the mbuf has our tag and the flag is set in it; FALSE otherwise.
 */

static boolean_t 
IsMBufTagFlagSet(mbuf_t m, MyMBufTagFlags flag)
{
    errno_t             status;
    MyMBufTagFlags *    flagPtr;
    size_t              len;

    assert(m != NULL);
    assert(flag != 0);

    status = mbuf_tag_find(m, gMyMBufTagID, kMyMBufTagTypeFlags, &len, (void**) &flagPtr);
    return (status == 0) && (len == sizeof(*flagPtr)) && (*flagPtr & flag);
}

/*! Sets the specified flag in our mbuf tag.
 *  \param m The mbuf whose tag we are setting.
 *  \param flag The flag to set.
 *  \returns An errno-style error code.
 */

static errno_t 
SetMBufTagFlag(mbuf_t m, MyMBufTagFlags flag)
{   
    errno_t             status;
    MyMBufTagFlags *    flagPtr;
    size_t              len;

    assert(m != NULL);
    assert(flag != 0);

    // Look for the existing tag.

    status = mbuf_tag_find(m, gMyMBufTagID, kMyMBufTagTypeFlags, &len, (void**) &flagPtr);
    if (status != 0) {

        // If it wasn't found, allocate it.

        // Because this code can be called on the packet processing path, we set MBUF_DONTWAIT 
        // when allocating mbuf tag memory to avoid the potential for deadlocks.

        status = mbuf_tag_allocate(m, gMyMBufTagID, kMyMBufTagTypeFlags, sizeof(*flagPtr), MBUF_DONTWAIT, (void**) &flagPtr);

        if (status == 0) {
            *flagPtr = 0;
        } else {
            printf("enetlognke err mbuf_tag_allocate failed -> %d\n", status);
        }
    } else {

        // If the tag exists, verify that its length makes sense.

        if (len != sizeof(*flagPtr)) {
            printf("enetlognke err incorrect tag length %lu/%lu\n", (unsigned long) len, (unsigned long) sizeof(*flagPtr));
            status = EINVAL;
        }
    }

    // If everything went OK, set the required flag.

    if (status == 0) {
        *flagPtr |= flag;
    }

    return status;
}

#pragma mark Packet Swallowing Subsystem

/*! Within the kernel all mutexes must bo placed in a group.  This is our reference 
 *  to that group.
 */

static lck_grp_t *  gMutexGroup = NULL;

/*! The queue structure which holds packets that have been swallowed.
 */

struct SwallowedPacket {
    TAILQ_ENTRY(SwallowedPacket)    qNext;
    ifnet_t                         interface;  ///< The interface of the swallowed packet; we've bumped the reference count on this interface.
    protocol_family_t               protocol;   ///< The protocol of the swallowed packet.
    mbuf_t                          firstMBuf;  ///< The swallowed packet itself.
};
typedef struct SwallowedPacket SwallowedPacket;

/*! A queue head for our swallowed packet queue.
 */

typedef struct SwallowedPacketQueue SwallowedPacketQueue;
TAILQ_HEAD(SwallowedPacketQueue, SwallowedPacket);

/*! This callback is called to re-inject a swallowed packet.
 *  \details If the routine succeeds it must take care of deallocating the packet mbuf.
 *  If it fails, it must not deallocate the packet mbuf chain; the caller will do so.
 *  \param queueItem The queue item containing information about the swallowed packet, including the packet itself.
 *  \returns An errno-style error code.
 */

typedef errno_t (*UnswallowProc)(const SwallowedPacket * queueItem);

/*! Holds the state associated with one side of the filter (either the input side or the output side).
 *  This includes a queue of packets, the mutex to provide safe access to that queue, and the 
 *  unswallow callback which is called to re-inject the packet.
 */

struct SwallowState {
    lck_mtx_t *             mutex;              ///< Protects the packetQueue field.
    SwallowedPacketQueue    packetQueue;        ///< Holds a queue of packets that have been swallowed.
    UnswallowProc           unswallowProc;      ///< Called to 'unswallow' a packet, that is, re-inject it into the stack.
    const char *            unswallowProcName;  ///< The name of the primary unswallow routine, for debugging.
};
typedef struct SwallowState SwallowState;

static SwallowState gInputSwallowState;         ///< The state for the input side of the filter.
static SwallowState gOutputSwallowState;        ///< The state for the output side of the filter.

static volatile SInt64 gBSDTimeoutsInFlight;    ///< The number of bsd_timeout calls in flight.

/*! Initialises one swallow state structure.
 *  \param swallowState The structure to initialise.
 *  \param unswallowProc The unswallow callback for this swallow state structure.
 *  \returns TRUE on success.
 */

static boolean_t
StartSwallowState(SwallowState * swallowState, UnswallowProc unswallowProc, const char * unswallowProcName)
{
    boolean_t   success;

    assert(swallowState != NULL);
    assert(unswallowProc != NULL);

    success = TRUE;

    swallowState->unswallowProc = unswallowProc;
    swallowState->unswallowProcName = unswallowProcName;

    TAILQ_INIT(&swallowState->packetQueue);

    swallowState->mutex = lck_mtx_alloc_init(gMutexGroup, LCK_ATTR_NULL);
    if (swallowState->mutex == NULL) {
        printf("enetlognke err lck_mtx_alloc_init\n");
        success = FALSE;
    }

    return success;
}

/*! Cleans up one swallow state structure.
 *  \param swallowState The structure to clean up.
 */

static void
StopSwallowState(SwallowState * swallowState)
{
    assert(swallowState != NULL);

    if (swallowState->mutex != NULL) {
        lck_mtx_free(swallowState->mutex, gMutexGroup);
        swallowState->mutex = NULL;
    }
    swallowState->unswallowProc = NULL;
    swallowState->unswallowProcName = NULL;
}

// forward declarations

static errno_t UnswallowInput (const SwallowedPacket * queueItem);
static errno_t UnswallowOutput(const SwallowedPacket * queueItem);

/*! Initialises the swallow subsystem as a whole.
 *  \param name The name to use for the lock group.
 *  \returns TRUE on success.
 */

static boolean_t
StartSwallowPacketSubsystem(const char * name)
{
    boolean_t   success;

    assert(kSwallowPackets);
    assert(name != NULL);

    success = TRUE;

    // Allocate our lock group.

    gMutexGroup = lck_grp_alloc_init(name, LCK_GRP_ATTR_NULL);
    if (gMutexGroup == NULL) {
        printf("enetlognke err lck_grp_alloc_init\n");
        success = FALSE;
    }

    // Allocate the input and output swallow states.

    if (success) {
        success = StartSwallowState(&gInputSwallowState,  UnswallowInput,  "ifnet_input");
    }
    if (success) {
        success = StartSwallowState(&gOutputSwallowState, UnswallowOutput, "ifnet_output_raw");
    }

    return success;
}

/*! Checks whether any of our bsd_timeout callbacks are in flight.
 *  \details This returns true if any of our bsd_timeout callbacks are running or waiting to 
 *  run.  It's unsafe to unload the KEXT in that case, so the KEXT stop routine calls this 
 *  before allowing the KEXT to unload.
 *
 *  IMPORTANT: This code is somewhat statistical.  Specifically, if SwallowTimerCallback (the 
 *  bsd_timeout callback routine) is suspended at LINE A and then we run, it's possible that 
 *  we could see gBSDTimeoutsInFlight being zero and allow the KEXT to unload.  At that point 
 *  the thread running SwallowTimerCallback resumes and runs code that's not there any more.
 *  It is possible to fix this (by switching away from the bsd_timeout timer mechanism) 
 *  but that would complicate the code more than I'm prepared to do for the sake of a 
 *  very-hard-to-reproducible problem in the KEXT unload path of a code sample.
 *
 *  I'm also not happy that this code accesses gBSDTimeoutsInFlight outside of a mutex and 
 *  thus risks problems on CPUs with weak memory models.  I'm not going to fix this because 
 *  a) the CPU supported by this sample, x86_64, does not have a weak memory model, and 
 *  b) the problem is likely to just go away with any proper fix to the previous problem.
 *
 *  \returns TRUE if any of our bsd_timeout callbacks are in flight.
 */

static boolean_t
IsSwallowTimerCallbackInFlight(void)
{
    return gBSDTimeoutsInFlight != 0;
}

/*! Cleans up the swallow subsystem as a whole.
 */

static boolean_t
StopSwallowPacketSubsystem(void)
{
    boolean_t       success;

    assert(kSwallowPackets);
    success = ! IsSwallowTimerCallbackInFlight();
    if (success) {
        StopSwallowState(&gInputSwallowState);
        StopSwallowState(&gOutputSwallowState);
        if (gMutexGroup != NULL) {
            lck_grp_free(gMutexGroup);
            gMutexGroup = NULL;
        }
    }
    return success;
}

/*! Called to re-inject packets on the input side of the filter
 *  \details See UnswallowProc for detailed information.
 */

static errno_t 
UnswallowInput(const SwallowedPacket * queueItem)
{
    assert(kSwallowPackets);
    assert(queueItem != NULL);
    return ifnet_input(queueItem->interface, queueItem->firstMBuf, NULL);
}

/*! Called to re-inject packets on the output side of the filter
 *  \details See UnswallowProc for detailed information.
 */

static errno_t 
UnswallowOutput(const SwallowedPacket * queueItem)
{
    assert(kSwallowPackets);
    assert(queueItem != NULL);
    return ifnet_output_raw(queueItem->interface, queueItem->protocol, queueItem->firstMBuf);
}

/*! Called to start the process of packet re-injection.
 *  \details This is called by both the input and output sides of the filter. 
 *  It's called by a timer (the timeout() routine) to re-inject the packets 
 *  that have been swallowed by the filter.  It works by removing packets 
 *  from the swallow state's packet queue and, for each one, calling the 
 *  unswallow callback to re-inject it.
 *  \param arg Actually a pointer to a swallow state structure, holding the state for 
 *  either the input or output sides of the filter.
 */

static void
SwallowTimerCallback(void * arg)
{
    errno_t             err;
    SwallowState *      swallowState;
    SwallowedPacket *   queueItem;

    assert(kSwallowPackets);
    assert(arg != NULL);

    // Recover the swallow state structure.

    swallowState = (SwallowState *) arg;

    // We need to hold the mutex while look at the queue, so let's start 
    // by taking that lock.

    lck_mtx_lock(swallowState->mutex);
    do {
        // Is there a first item in the queue?  If not, we're done.  If so, remove it.

        queueItem = TAILQ_FIRST(&swallowState->packetQueue);
        if (queueItem == NULL) {
            break;
        }
        TAILQ_REMOVE(&swallowState->packetQueue, queueItem, qNext);

        // Release the mutex because the unswallow proc is going to call into the 
        // system and we don't want to be holding a mutex while doing that.

        lck_mtx_unlock(swallowState->mutex);

        // Unswallow the packet and, if that fails, free the packet ourselves.

        err = swallowState->unswallowProc(queueItem);
        if (err != 0) {
            printf("enetlognke err %s -> %d; dropping packet\n", swallowState->unswallowProcName, err);
            mbuf_freem(queueItem->firstMBuf);
        }
        queueItem->firstMBuf = NULL;

        // Release the reference to the interface that we took in SwallowPacketCommon.
        // Then clear out all the other fields in the queue item, just to keep things neat.

        ifnet_release(queueItem->interface);
        queueItem->interface = NULL;
        queueItem->protocol = 0;

        // Free the queue item itself.

        OSFree(queueItem, sizeof(SwallowedPacket), gOSMallocTag);

        // Reacquire the mutex so that the while conditional is safe.

        lck_mtx_lock(swallowState->mutex);
    } while (TRUE);
    lck_mtx_unlock(swallowState->mutex);

    OSDecrementAtomic64(&gBSDTimeoutsInFlight);
    // LINE A -- See comment in IsSwallowTimerCallbackInFlight.
}

/*! Common code for packet swallowing.
 *  \details This is called by both the input (SwallowPacketInput) and output 
 *  (SwallowPacketOutput) sides of the filter.  It stashes a reference to the 
 *  packet in the swallow state structure and then kicks off a timer to 
 *  re-inject the swallowed packet at some point in the future.
 *
 *  If there's a problem saving the packet, the routine simple drops it.  This 
 *  makes the memory management for the caller easy.
 *
 *  \param interface The interface for this packet.
 *  \param protocol The protocol for this packet.
 *  \param m The packet itself.
 *  \param swallowState A pointer to a swallow state structure, holding the state for 
 *  either the input or output sides of the filter.
 */

static void 
SwallowPacketCommon(
    ifnet_t                 interface, 
    protocol_family_t       protocol, 
    mbuf_t                  m, 
    SwallowState *          swallowState
)
{
    SwallowedPacket *   queueItem;
    struct timespec     ts;
    errno_t             err;

    assert(kSwallowPackets);
    assert(interface != NULL);
    // nothing to say about protocol
    assert(m != NULL);
    assert(swallowState != NULL);

    // Allocate a queue entry so that we can store the packet on our swallow queue.
    // 
    // Note: We don't need to use the OSMalloc_nowait and OSMalloc_noblock variants of OSMalloc
    // because OSMalloc will not deadlock with the packet processing call.

    queueItem = (SwallowedPacket *) OSMalloc(sizeof(SwallowedPacket), gOSMallocTag);
    if (queueItem == NULL) {
        printf("enetlognke err OSMalloc; dropping packet\n");
        mbuf_freem(m);
    } else {
        // Fill out the queue structure.

        queueItem->interface = interface;
        queueItem->protocol  = protocol;
        queueItem->firstMBuf = m;

        // Take a reference on the interface; we'll drop this when when we're done 
        // with the packet.

        err = ifnet_reference(queueItem->interface);
        assert(err == 0);

        // Queue the item into the specified queue for processing when the timer fires.

        lck_mtx_lock(swallowState->mutex);
        TAILQ_INSERT_TAIL(&swallowState->packetQueue, queueItem, qNext);
        lck_mtx_unlock(swallowState->mutex);

        // Initiate timer action in 10 microsec.

        OSIncrementAtomic(&gBSDTimeoutsInFlight);
        ts.tv_sec = 0;
        ts.tv_nsec = 10000;
        bsd_timeout(SwallowTimerCallback, swallowState, &ts); 
    }
}

/*! Swallows a packet on the input side of the filter.
 *  \details See SwallowPacketCommon for details.
 */

static void 
SwallowPacketInput(ifnet_t interface, protocol_family_t protocol, mbuf_t m)
{
    assert(kSwallowPackets);
    SwallowPacketCommon(interface, protocol, m, &gInputSwallowState );
}

/*! Swallows a packet on the output side of the filter.
 *  \details See SwallowPacketCommon for details.
 */

static void 
SwallowPacketOutput(ifnet_t interface, protocol_family_t protocol, mbuf_t m)
{
    assert(kSwallowPackets);
    SwallowPacketCommon(interface, protocol, m, &gOutputSwallowState);
}

#pragma mark * Filter Subsystem

/*! A reference to our filter.  We get this when we attach the filter and then 
 *  use it to detach.
 */

static interface_filter_t   gInterfaceFilter;

static boolean_t            gFilterAttached  = FALSE;       ///< This will be TRUE if the filter is currently attached.
static boolean_t            gFilterDetaching = FALSE;       ///< This will be TRUE if the filter is in the process of being detached.
static boolean_t            gFilterDetached  = FALSE;       ///< This will be TRUE if the filter is fully detached.

/*! Allows the interface filter to filter incoming packets.
 *  \details See iff_input_func for detailed information.
 */

static errno_t 
enetlognke_input_func(
    void*               cookie, 
    ifnet_t             interface, 
    protocol_family_t   protocol,
    mbuf_t *            data, 
    char **             framePtrPtr)
{
    #pragma unused(cookie)
    errno_t         err;
    boolean_t       seenItBefore;

    assert(interface != NULL);
    // nothing to say about protocol
    assert(data != NULL);
    assert(*data != NULL);
    assert(framePtrPtr != NULL);
    assert(*framePtrPtr != NULL);

    err = 0;

    // Check if we've seen this packet before.

    seenItBefore = IsMBufTagFlagSet(*data, kMyMBufTagFlagsInputDone);

    // If logging is enabled, log the packet.

    if (kLogPacketByteCount != 0) {
        PrintPacketSummary("in ", protocol, *framePtrPtr, ifnet_hdrlen(interface), *data, seenItBefore);
    }

    // If we haven't seen the packet before, process it.

    if ( ! seenItBefore ) {

        // If we, or any other filter, swallows the packet and later re-injects it, we have 
        // to be prepared to see the packet pass through this routine once again.  To avoid 
        // working on these duplicate packets, we tag the mbuf so that we can tell if we have 
        // processed this packet before.

        err = SetMBufTagFlag(*data, kMyMBufTagFlagsInputDone);

        // If the tagged failed, we leave the error in err.  This will cause the system 
        // to stop processing this packet.  OTOH, if the tagging succeeded, we then 
        // need to decide whether swallowing is required.

        if (err == 0) {
            if (kSwallowPackets) {

                // Before we swallow an input packet, we need to make sure that the very first mbuf
                // has the packet header field set, otherwise the system will panic when we re-inject
                // the packet.  This input routine is passed the frame header pointer, so we can use
                // that value as the packet header.

                if (mbuf_pkthdr_header(*data) == NULL) {
                    mbuf_pkthdr_setheader(*data, *framePtrPtr);
                }
                // ifnet_hdrlen

                SwallowPacketInput(interface, protocol, *data);

                // The above routine has taken care of the packet (it's either been queued 
                // for later re-injection or, if the queuing failed, it's been dropped).  
                // We tell the caller to just return, that is, to no longer process this packet 
                // in any way.

                err = EJUSTRETURN;
            }
        }
    }

    return err;
}

/*! Allows the interface filter to filter outgoing packets.
 *  \details See iff_output_func for detailed information.
 */

static errno_t 
enetlognke_output_func(
    void *              cookie, 
    ifnet_t             interface, 
    protocol_family_t   protocol,
    mbuf_t *            data
)
{
    #pragma unused(cookie)
    errno_t         err;
    boolean_t       seenItBefore;

    assert(interface != NULL);
    // nothing to say about protocol
    assert(data != NULL);
    assert(*data != NULL);

    err = 0;

    // Check if we've seen this packet before.

    seenItBefore = IsMBufTagFlagSet(*data, kMyMBufTagFlagsOutputDone);

    // If logging is enabled, log the packet.

    if (kLogPacketByteCount != 0) {
        PrintPacketSummary("out", protocol, NULL, 0, *data, seenItBefore);
    }

    // If we haven't seen the packet before, process it.

    if ( ! seenItBefore ) {

        // If we, or any other filter, swallows the packet and later re-injects it, we have 
        // to be prepared to see the packet pass through this routine once again.  To avoid 
        // printing these duplicate packets, we tag the mbuf so that we can tell if we have 
        // processed this packet before.

        err = SetMBufTagFlag(*data, kMyMBufTagFlagsOutputDone);

        // If the tagged failed, we leave the error in err.  This will cause the system 
        // to stop processing this packet.  OTOH, if the tagging succeeded, we then 
        // need to decide whether swallowing is required.

        if (err == 0) {
            if (kSwallowPackets) {
                SwallowPacketOutput(interface, protocol, *data);

                // The above routine has taken care of the packet (it's either been queued 
                // for later re-injection or, if the queuing failed, it's been dropped).  
                // We tell the caller to just return, that is, to no longer process this packet 
                // in any way.

                err = EJUSTRETURN;
            }
        }
    }

    return err;
}

/*! Allows the interface filter to hear about events related to the interface.
 *  \details See iff_event_func for detailed information.
 *  \note Due to a bug <rdar://problem/16342178>, some events that you might 
 *  expect to be delivered here are not (for example, KEV_DL_IF_DETACHING).
 */

static void 
enetlognke_event_func(
    void *                  cookie, 
    ifnet_t                 interface, 
    protocol_family_t       protocol,
    const struct kev_msg *  event
)
{
    #pragma unused(cookie)
    #pragma unused(interface)
    #pragma unused(protocol)
    char                protocolName[16];

    assert(interface != NULL);
    // nothing to say about protocol
    assert(event != NULL);

    ProtocolToString(protocol, protocolName, sizeof(protocolName));
    printf("enetlognke event protocol:%s vendor:%u class:%u subclass:%u code:%u\n",
        protocolName,  
        (unsigned int) event->vendor_code,  
        (unsigned int) event->kev_class, 
        (unsigned int) event->kev_subclass, 
        (unsigned int) event->event_code
    );
}

/*! Allows the interface filter to filter ioctls sent to the interface.
 *  \details See iff_ioctl_func for detailed information.
 */

static errno_t 
enetlognke_ioctl_func(
    void *                  cookie, 
    ifnet_t                 interface, 
    protocol_family_t       protocol,
    unsigned long           command, 
    void *                  argument
)
{
    #pragma unused(cookie)
    #pragma unused(interface)
    #pragma unused(argument)
    char                protocolName[16];

    assert(interface != NULL);
    // nothing to say about protocol, command, or argument

    ProtocolToString(protocol, protocolName, sizeof(protocolName));
    printf("enetlognke ioctl protocol:%s command:0x%lx\n", protocolName, command);
    return EOPNOTSUPP;
}

/*! Called to notify the filter that it has been detached from an interface.
 *  \details See iff_detached_func for detailed information.
 */

static void 
enetlognke_detached_func(void* cookie, ifnet_t interface)
{
    #pragma unused(cookie)
    #pragma unused(interface)
    printf("enetlognke detached\n");
    gFilterAttached  = FALSE;
    gFilterDetaching = FALSE;
    gFilterDetached  = TRUE;
}

/*! Describes the interface filter to the system.
 */

static struct iff_filter gInterfaceFilterInfo = {
    NULL,                       // not using the cookie
    MYBUNDLEID,
    0,                          // interested in all protocol packets
    enetlognke_input_func,
    enetlognke_output_func,
    enetlognke_event_func,
    enetlognke_ioctl_func,
    enetlognke_detached_func
};

/*! Initialise the interface filter subsystem.
 *  \returns TRUE on success.
 */

static boolean_t 
StartFilterSubsystem(void)
{
    boolean_t       success;
    ifnet_t         interface;
    errno_t         err;

    success = TRUE;

    // First try to find our interface.

    err = ifnet_find_by_name(gNameOfInterfaceToFilter, &interface);
    if (err != 0) {
        printf("enetlognke err ifnet_find_by_name -> %d\n", err);
        success = FALSE;
    }

    // If that succeeds, register the filter on it.

    if (success) {
        err = iflt_attach(interface, &gInterfaceFilterInfo, &gInterfaceFilter);
        if (err != 0) {
            printf("enetlognke err iflt_attach -> %d\n", err);
            success = FALSE;
        }

        (void) ifnet_release(interface);        // releases the reference returned by ifnet_find_by_name
    }

    if (success) {
        gFilterAttached = TRUE;
    }

    return success;
}

/*! Cleans up the interface filter subsystem.
 *  \returns TRUE on success, implying that the KEXT as a whole can be unloaded.
 */

static boolean_t 
StopFilterSubsystem(void)
{
    boolean_t       success;

    if (gFilterAttached) {

        // Make sure we only start the detach process once.

        if ( ! gFilterDetaching ) {
            iflt_detach(gInterfaceFilter);
            gFilterDetaching = TRUE;
        }

        // It's common for the detach to finish very quickly.  If that's the case 
        // we return TRUE so that the KEXT can unload immediately.

        success = gFilterDetached;
    } else {
        success = TRUE;
    }
    return success;
}

/* =================================== */
#pragma mark kext entry points

// prototypes to keep the compiler happy

extern kern_return_t com_example_apple_samplecode_kext_enetlognke_start(kmod_info_t * ki, void * d);
extern kern_return_t com_example_apple_samplecode_kext_enetlognke_stop (kmod_info_t * ki, void * d);

/*! Called by the system to start the KEXT.
 *  \returns KERN_SUCCESS on success; some other error otherwise.
 */

extern kern_return_t com_example_apple_samplecode_kext_enetlognke_start(kmod_info_t * ki, void * d) 
{
    boolean_t       success;

    printf("enetlognke start '%s'\n", gNameOfInterfaceToFilter);

    if (FALSE) {
        PE_enter_debugger("enetlognke start");
    }

    // If any of these are set it means that we've been started twice.  Previous versions 
    // of the code protected against that.  However, it makes no sense so I've replaced 
    // that protection with asserts.

    assert( ! gFilterAttached );
    assert( ! gFilterDetaching );
    assert( ! gFilterDetached );

    success = StartMemorySubsystem(gInterfaceFilterInfo.iff_name);
    if (success) {
        success = StartMBufTagSubsystem(gInterfaceFilterInfo.iff_name);
    }
    if (success && kSwallowPackets) {
        success = StartSwallowPacketSubsystem(gInterfaceFilterInfo.iff_name);
    }
    if (success) {
        success = StartFilterSubsystem();
    }

    if ( ! success ) {
        // If we failed to start we call our own stop routine to clean up 
        // any wreckage.
        (void) com_example_apple_samplecode_kext_enetlognke_stop(ki, d);
    }

    return success ? KERN_SUCCESS : KERN_FAILURE;
}

/*! Called by the system to stop the KEXT.
 *  \details If this fails the KEXT will not be unloaded.
 *  \returns KERN_SUCCESS on success; some other error otherwise.
 */

extern kern_return_t com_example_apple_samplecode_kext_enetlognke_stop (kmod_info_t * ki, void * d) 
{
    #pragma unused(ki)
    #pragma unused(d)
    boolean_t           success;

    // First try to stop the filter subsystem.  This can fail if the filter doesn't 
    // detach immediately.

    success = StopFilterSubsystem();
    if ( ! success ) {
        printf("enetlognke stop failed; could not stop filter\n");
    }

    // If that succeeds, continue shutting things down.  If we're swallowing packets, 
    // shut down that subsystem.  We can fail here because there might be packets in 
    // flight (that is, that have been queue but not yet delivered).

    if (success) {
        if (kSwallowPackets) {
            success = StopSwallowPacketSubsystem();
            if ( ! success ) {
                printf("enetlognke stop failed; swallowed packets in flight\n");
            }
        }
    }

    // Continue shutting down some more.  None of the rest of the following code can 
    // fail.

    if (success) {
        // There is no StopMBufTagSubsystem because mbuf tag IDs can't be deallocated.
        StopMemorySubsystem();
    }

    if (success) {
        printf("enetlognke stop succeeded\n");
    } else {
        // Do nothing here; any failure code path has already printed an explanation.
    }

    return success ? KERN_SUCCESS : KERN_FAILURE;
}
```

[Next](Read%20Me.txt.md)[Previous](enetlognke.md)

