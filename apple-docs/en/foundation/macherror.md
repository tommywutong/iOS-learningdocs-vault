---
title: MachError
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/macherror
source_url: 'https://developer.apple.com/documentation/foundation/macherror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/macherror.json'
content_hash: 'sha256:4c3777c6ebd59911'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# MachError

<sub>Structure</sub>

Describes an error in the Mach error domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MachError
```

## Relationships

- **Conforms To**: [CustomNSError](customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Aliases

- [Code](macherror/code.md) — The type of an error code.

### Type Properties

- [aborted](macherror/aborted.md) — The operation was aborted.  Ipc code will catch this and reflect it as a message error.
- [alreadyInSet](macherror/alreadyinset.md) — The receive right is already a member of the portset.
- [alreadyWaiting](macherror/alreadywaiting.md) — A thread is attempting to wait for an event for which there is already a waiting thread.
- [codesignError](macherror/codesignerror.md) — During a page fault, indicates that the page was rejected as a result of a signature check.
- [defaultSet](macherror/defaultset.md) — An attempt was made to destroy the default processor set.
- [exceptionProtected](macherror/exceptionprotected.md) — An attempt was made to fetch an exception port that is protected, or to abort a thread while processing a protected exception.
- [failure](macherror/failure.md) — The function could not be performed.  A catch-all.
- [invalidAddress](macherror/invalidaddress.md) — Specified address is not currently valid.
- [invalidArgument](macherror/invalidargument.md) — The function requested was not applicable to this type of argument, or an argument is invalid.
- [invalidCapability](macherror/invalidcapability.md) — The supplied (port) capability is improper.
- [invalidHost](macherror/invalidhost.md) — Target host isn’t actually a host.
- [invalidLedger](macherror/invalidledger.md) — A ledger was required but not supplied.
- [invalidMemoryControl](macherror/invalidmemorycontrol.md) — The port was not a memory cache control port.
- [invalidName](macherror/invalidname.md) — The name doesn’t denote a right in the task.
- [invalidObject](macherror/invalidobject.md) — The external memory manager failed to initialize the memory object.
- [invalidPolicy](macherror/invalidpolicy.md) — The specified scheduling policy is not currently enabled for the processor set.
- [invalidProcessorSet](macherror/invalidprocessorset.md) — An argument applied to assert processor set privilege was not a processor set control port.
- [invalidRight](macherror/invalidright.md) — The name denotes a right, but not an appropriate right.
- [invalidSecurity](macherror/invalidsecurity.md) — An argument supplied to assert security privilege was not a host security port.
- [invalidTask](macherror/invalidtask.md) — Target task isn’t an active task.
- [invalidValue](macherror/invalidvalue.md) — A blatant range error.
- [lockOwned](macherror/lockowned.md) — The lock is already owned by another thread.
- [lockOwnedSelf](macherror/lockownedself.md) — The lock is already owned by the calling thread.
- [lockSetDestroyed](macherror/locksetdestroyed.md) — Lock set has been destroyed and is no longer available.
- [lockUnstable](macherror/lockunstable.md) — The thread holding the lock terminated before releasing the lock.
- [memoryDataMoved](macherror/memorydatamoved.md) — A page was requested of a memory manager via memory_object_data_request for an object using a MEMORY_OBJECT_COPY_CALL strategy, with the VM_PROT_WANTS_COPY flag being used to specify that the page desired is for a copy of the object, and the memory manager has detected the page was pushed into a copy of the object while the kernel was walking the shadow chain from the copy to the object. This error code is delivered via memory_object_data_error and is handled by the kernel (it forces the kernel to restart the fault). It will not be seen by users.
- [memoryError](macherror/memoryerror.md) — During a page fault, the memory object indicated that the data could not be returned.  This failure may be temporary; future attempts to access this same data may succeed, as defined by the memory object.
- [memoryFailure](macherror/memoryfailure.md) — During a page fault, the target address refers to a memory object that has been destroyed.  This failure is permanent.
- [memoryPresent](macherror/memorypresent.md) — An attempt was made to supply “precious” data for memory that is already present in a memory object.
- [memoryRestartCopy](macherror/memoryrestartcopy.md) — A strategic copy was attempted of an object upon which a quicker copy is now possible.  The caller should retry the copy using vm_object_copy_quickly. This error code is seen only by the kernel.
- [nameExists](macherror/nameexists.md) — The name already denotes a right in the task.
- [noAccess](macherror/noaccess.md) — Bogus access restriction.
- [noSpace](macherror/nospace.md) — The address range specified is already in use, or no address range of the size specified could be found.
- [nodeDown](macherror/nodedown.md) — Remote node down or inaccessible.
- [notDepressed](macherror/notdepressed.md) — thread_depress_abort was called on a thread which was not currently depressed.
- [notInSet](macherror/notinset.md) — The receive right is not a member of a port set.
- [notReceiver](macherror/notreceiver.md) — The task in question does not hold receive rights for the port argument.
- [notSupported](macherror/notsupported.md) — Empty thread activation (No thread linked to it).
- [notWaiting](macherror/notwaiting.md) — A signalled thread was not actually waiting.
- [operationTimedOut](macherror/operationtimedout.md) — Some thread-oriented operation (semaphore_wait) timed out.
- [policyLimit](macherror/policylimit.md) — The specified scheduling attributes exceed the thread’s limits.
- [policyStatic](macherror/policystatic.md) — The requested property cannot be changed at this time.
- [protectionFailure](macherror/protectionfailure.md) — Specified memory is valid, but does not permit the required forms of access.
- [resourceShortage](macherror/resourceshortage.md) — A system resource could not be allocated to fulfill this request.  This failure may not be permanent.
- [rightExists](macherror/rightexists.md) — The task already has send or receive rights for the port under another name.
- [rpcContinueOrphan](macherror/rpccontinueorphan.md) — Allow an orphaned activation to continue executing.
- [rpcServerTerminated](macherror/rpcserverterminated.md) — Return from RPC indicating the target server was terminated before it successfully replied.
- [rpcTerminateOrphan](macherror/rpcterminateorphan.md) — Terminate an orphaned activation.
- [semaphoreDestroyed](macherror/semaphoredestroyed.md) — Semaphore has been destroyed and is no longer available.
- [success](macherror/success.md)
- [terminated](macherror/terminated.md) — Object has been terminated and is no longer available.
- [userReferencesOverflow](macherror/userreferencesoverflow.md) — Operation would overflow limit on user-references.

## See Also

### Error Codes

- [CocoaError](cocoaerror.md) — Describes errors within the Cocoa error domain.
- [POSIXError](posixerror.md) — Describes an error in the POSIX error domain.
- [NSError Codes](1448136-nserror-codes.md) — Error codes in the Cocoa error domain.
