---
title: Descriptor Passing Problems
apple_id: DTS10004423
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-10-29'
source_url: https://developer.apple.com/library/archive/qa/qa1541/_index.html
archived_at: '2026-07-18T02:32:15.696245Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1541

# Descriptor Passing Problems

## Q:  I'm passing multiple file descriptors from one process to another over a UNIX domain socket. Sometimes the receiving process only gets the first one. Is this is a known problem?

A: I'm passing multiple file descriptors from one process to another over a UNIX domain socket. Sometimes the receiving process only gets the first one. Is this is a known problem?

Yes. Mac OS X 10.5 fixes a number of kernel bugs related to descriptor passing
(rr. 4650646, 5232558 and 5232524)
. On earlier systems you must take steps to avoid these bugs.

- Always pass descriptors over a stream-based socket (`SOCK_STREAM`). It is possible to pass descriptors over a datagram-based socket (`SOCK_DGRAM`) but the kernel does not guarantee delivery of the message, and hence its associated descriptor.
- Avoid writing descriptors to a full socket. In some circumstances the message, and its associated descriptor, might get dropped.
- Avoid passing two or more descriptors back-to-back. If you need to do this, acknowledge each descriptor as you pass it. Listing 1 shows one way to do this.

__Listing 1__  The safest way to pass descriptors

```
// When we pass a descriptor, we have to pass at least one byte  // of data along with it, otherwise the recvmsg call will not  // block if the descriptor hasn't been written to the other end  // of the socket yet.  static const char kDummyData = 'D';  // Due to a kernel bug in Mac OS X 10.4.x and earlier  // <rdar://problem/4650646>, you will run into problems if you write  // data to a socket while a process is trying to receive a descriptor  // from that socket. A common symptom of this problem is that, if  // you write two descriptors back-to-back, the second one just  // disappears. // // To avoid this problem, we explicitly ACK all descriptor transfers.  // After writing a descriptor, the sender reads an ACK byte from the  // socket. After reading a descriptor, the receiver sends an ACK byte  // (kACKData) to unblock the sender.  static const char kACKData   = 'A';  static bool kWorkaround4650646 = true;  static int ReadDescriptor(int fd, int *fdRead)     // Read a descriptor from fd and place it in *fdRead.     //     // On success, the caller is responsible for closing *fdRead. {     int                 err;     int                 junk;     struct msghdr       msg;     struct iovec        iov;     struct {         struct cmsghdr  hdr;         int             fd;     }                   control;     char                dummyData;     ssize_t             bytesReceived;      // Pre-conditions      assert(fd >= 0);     assert( fdRead != NULL);     assert(*fdRead == -1);      // Read a single byte of data from the socket, with the assumption      // that this byte has piggybacked on to it a single descriptor that      // we're trying to receive. This is pretty much standard boilerplate      // code for reading descriptors; see <x-man-page://2/recv> for details.      iov.iov_base = (char *) &dummyData;     iov.iov_len  = sizeof(dummyData);      msg.msg_name       = NULL;     msg.msg_namelen    = 0;     msg.msg_iov        = &iov;     msg.msg_iovlen     = 1;     msg.msg_control    = &control;     msg.msg_controllen = sizeof(control);     msg.msg_flags      = MSG_WAITALL;      do {         bytesReceived = recvmsg(fd, &msg, 0);         if (bytesReceived == sizeof(dummyData)) {             if ( (dummyData != kDummyData)                 || (msg.msg_flags != 0)                  || (msg.msg_control == NULL)                  || (msg.msg_controllen != sizeof(control))                  || (control.hdr.cmsg_len != sizeof(control))                  || (control.hdr.cmsg_level != SOL_SOCKET)                 || (control.hdr.cmsg_type  != SCM_RIGHTS)                  || (control.fd < 0) ) {                 err = EINVAL;             } else {                 *fdRead = control.fd;                 err = 0;             }         } else if (bytesReceived == 0) {             err = EPIPE;         } else {             assert(bytesReceived == -1);              err = errno;             assert(err != 0);         }     } while (err == EINTR);      // Send the ACK. If that fails, we have to act like we never got the      // descriptor in our to ensure consistent results for our caller.      if ( (err == 0) && kWorkaround4650646) {         do {             if ( write(fd, &kACKData, sizeof(kACKData)) == -1 ) {                 err = errno;             }         } while (err == EINTR);          if (err != 0) {             junk = close(*fdRead);             assert(junk == 0);             *fdRead = -1;         }     }      // Post condition      assert( (err == 0) == (*fdRead >= 0) );      return err; }  static int WriteDescriptor(int fd, int fdToWrite)     // Write the descriptor fdToWrite to fd. {     int                 err;     struct msghdr       msg;     struct iovec        iov;     struct {         struct cmsghdr  hdr;         int             fd;     }                   control;     ssize_t             bytesSent;     char                ack;      // Pre-conditions      assert(fd >= 0);     assert(fdToWrite >= 0);      control.hdr.cmsg_len   = sizeof(control);     control.hdr.cmsg_level = SOL_SOCKET;     control.hdr.cmsg_type  = SCM_RIGHTS;     control.fd             = fdToWrite;      iov.iov_base = (char *) &kDummyData;     iov.iov_len  = sizeof(kDummyData);      msg.msg_name       = NULL;     msg.msg_namelen    = 0;     msg.msg_iov        = &iov;     msg.msg_iovlen     = 1;     msg.msg_control    = &control;     msg.msg_controllen = control.hdr.cmsg_len;     msg.msg_flags      = 0;     do {         bytesSent = sendmsg(fd, &msg, 0);         if (bytesSent == sizeof(kDummyData)) {             err = 0;         } else {             assert(bytesSent == -1);              err = errno;             assert(err != 0);         }     } while (err == EINTR);      // After writing the descriptor, try to read an ACK back from the      // recipient. If that fails, or we get the wrong ACK, we've failed.      if ( (err == 0) && kWorkaround4650646 ) {         do {             ssize_t     bytesRead;              bytesRead = read(fd, &ack, sizeof(ack));             if (bytesRead == 0) {                 err = EPIPE;             } else if (bytesRead == -1) {                 err = errno;             }         } while (err == EINTR);          if ( (err == 0) && (ack != kACKData) ) {             err = EINVAL;         }     }      return err; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-10-29 | New document that describes how to work around common problems with descriptor passing. |

