---
title: FSDeleteObject fails with fBsyErr, sometimes
apple_id: DTS10004155
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2008-09-24'
source_url: https://developer.apple.com/library/archive/qa/qa1497/_index.html
archived_at: '2026-07-18T02:31:37.905975Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1497

# FSDeleteObject fails with fBsyErr, sometimes

## Q:  I'm writing some 'safe save' code. When I delete my temporary file, `FSDeleteObject` fails with `fBsyErr` (-47), but only sometimes. If I delay for a few seconds and then retry, it works. What's going on?

A: I'm writing some 'safe save' code. When I delete my temporary file, `FSDeleteObject` fails with `fBsyErr` (-47), but only sometimes. If I delay for a few seconds and then retry, it works. What's going on?

There are two common causes for this problem, each described in a subsequent section. However, let's start with some background information.

- The Mac OS X kernel supports two delete code paths: unlink and `FSDeleteObject`.
- The `unlink` code path implements the traditional UNIX semantics of allowing you to delete open files.
- `FSDeleteObject` implements the traditional Mac OS semantics of returning an error if the file is open. This error is `EBUSY`, which File Manager translates to `fBsyErr`.
- When you close a modified file, the kernel generates a notification that, amongst other things, causes Spotlight to start indexing the file.

The most common cause of `FSDeleteObject` temporarily failing with `fBsyErr` is that Spotlight is in the process of indexing the file. If you modify a file, close it, and then immediately try to delete it using `FSDeleteObject`, it's quite possible that the Spotlight indexer will have it open and you'll get `fBsyErr`.

There are numerous ways to prevent this problem.

1. If, when you create the file, you know that it shouldn't be indexed (for example, in your case, you know that it's a safe save temporary), create it somewhere that Spotlight won't index, or with a name that causes it not to be indexed.

   Places that won't get indexed by Spotlight include:

   - The standard UNIX temporary directory (`/tmp`)
   - The temporary items folder returned by Folder Manager with the `kTemporaryFolderType` selector

   Names that won't get indexed include:

   - Names beginning with a "."
   - Names ending with ".noindex"

   These lists are not exhaustive
   (r. 4823573)
   because the full list of what Spotlight doesn't index is likely to change over time. However, if you use one of the techniques listed above, you should be compatible with any future system.
2. The preceeding technique won't work if you can't tell, in advance, whether the file will persist (and need to be indexed) or not. In that case, if you know you've modified the file but it doesn't need to persist, delete the file (using `unlink` or `FSUnlinkObject`) before you close it. That way the Spotlight indexer will never be invoked.
3. Alternatively, always delete files using unlink or `FSUnlinkObject`.
4. When `FSDeleteObject` fails with `fBsyErr`, delay for a short period of time and then retry.

Some third party anti-virus scanners can also trigger this problem. When you close a modified file, the anti-virus scanner immediately starts to check it for viruses. If it's still checking when you try to delete the file, `FSDeleteObject` will fail with `fBsyErr`.

In this case, the first workaround (option 1 in the previous section) will not work because there are no standard locations or names that prevent anti-virus scanning; you will have to use one of the other options.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-24 | Added note to indicate that as of 10.5 (Leopard) - a new File Manager API was added and added the description of it. Cleaned up grammatical issues. |
| 2006-11-17 | New document that why Spotlight indexing can cause file deletion to fail, and what to do about it. |

