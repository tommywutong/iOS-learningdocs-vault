---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_15.html
archived_at: '2026-07-15T07:31:03.740883Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Porting%20GDB.md), [next](Releasing%20GDB.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Versions and Branches](GDB%20Internals.md#apple-krhugmjsgq)

## [Versions](GDB%20Internals.md#apple-krhugmjsgu)

GDB's version is determined by the file
`gdb/version.in' and takes one of the following forms:

**major.minor**
:

**major.minor.patchlevel**
: an official release (e.g., 6.2 or 6.2.1)

**major.minor.patchlevel.YYYYMMDD**
: a snapshot taken at YYYY-MM-DD-gmt (e.g.,
6.1.50.20020302, 6.1.90.20020304, or 6.1.0.20020308)

**major.minor.patchlevel.YYYYMMDD-cvs**
: a CVS check out drawn on YYYY-MM-DD (e.g.,
6.1.50.20020302-cvs, 6.1.90.20020304-cvs, or 6.1.0.20020308-cvs)

**major.minor.patchlevel.YYYYMMDD (vendor)**
: a vendor specific release of GDB, that while based on
major.minor.patchlevel.YYYYMMDD,
may include additional changes

GDB's mainline uses the major and minor version
numbers from the most recent release branch, with a patchlevel
of 50. At the time each new release branch is created, the mainline's
major and minor version numbers are updated.

GDB's release branch is similar. When the branch is cut, the
patchlevel is changed from 50 to 90. As draft releases are
drawn from the branch, the patchlevel is incremented. Once the
first release (major.minor) has been made, the
patchlevel is set to 0 and updates have an incremented
patchlevel.

For snapshots, and CVS check outs, it is also possible to
identify the CVS origin:

**major.minor.50.YYYYMMDD**
: drawn from the HEAD of mainline CVS (e.g., 6.1.50.20020302)

**major.minor.90.YYYYMMDD**
:

**major.minor.91.YYYYMMDD ...**
: drawn from a release branch prior to the release (e.g.,
6.1.90.20020304)

**major.minor.0.YYYYMMDD**
:

**major.minor.1.YYYYMMDD ...**
: drawn from a release branch after the release (e.g., 6.2.0.20020308)

If the previous GDB version is 6.1 and the current version is
6.2, then, substituting 6 for major and 1 or 2 for minor,
here's an illustration of a typical sequence:

```
     <HEAD>
        |
6.1.50.20020302-cvs
        |
        +--------------------------.
        |                    <gdb_6_2-branch>
        |                          |
6.2.50.20020303-cvs        6.1.90 (draft #1)
        |                          |
6.2.50.20020304-cvs        6.1.90.20020304-cvs
        |                          |
6.2.50.20020305-cvs        6.1.91 (draft #2)
        |                          |
6.2.50.20020306-cvs        6.1.91.20020306-cvs
        |                          |
6.2.50.20020307-cvs        6.2 (release)
        |                          |
6.2.50.20020308-cvs        6.2.0.20020308-cvs
        |                          |
6.2.50.20020309-cvs        6.2.1 (update)
        |                          |
6.2.50.20020310-cvs         <branch closed>
        |
6.2.50.20020311-cvs
        |
        +--------------------------.
        |                     <gdb_6_3-branch>
        |                          |
6.3.50.20020312-cvs        6.2.90 (draft #1)
        |                          |
```

## [Release Branches](GDB%20Internals.md#apple-krhugmjsgy)

GDB draws a release series (6.2, 6.2.1, ...) from a
single release branch, and identifies that branch using the CVS
branch tags:

```
gdb_major_minor-YYYYMMDD-branchpoint
gdb_major_minor-branch
gdb_major_minor-YYYYMMDD-release
```

_Pragmatics: To help identify the date at which a branch or
release is made, both the branchpoint and release tags include the
date that they are cut (YYYYMMDD) in the tag. The
branch tag, denoting the head of the branch, does not need this._

## [Vendor Branches](GDB%20Internals.md#apple-krhugmjsg4)

To avoid version conflicts, vendors are expected to modify the file
`gdb/version.in' to include a vendor unique alphabetic identifier
(an official GDB release never uses alphabetic characters in
its version identifer). E.g., `` `6.2widgit2' ``, or `` `6.2 (Widgit
Inc Patch 2)' ``.

## [Experimental Branches](GDB%20Internals.md#apple-krhugmjsha)

### [Guidelines](GDB%20Internals.md#apple-krhugmjshe)

GDB permits the creation of branches, cut from the CVS
repository, for experimental development. Branches make it possible
for developers to share preliminary work, and maintainers to examine
significant new developments.

The following are a set of guidelines for creating such branches:

**_a branch has an owner_**
: The owner can set further policy for a branch, but may not change the
ground rules. In particular, they can set a policy for commits (be it
adding more reviewers or deciding who can commit).

**_all commits are posted_**
: All changes committed to a branch shall also be posted to
@email{gdb-patches@sources.redhat.com, the GDB patches
mailing list}. While commentary on such changes are encouraged, people
should remember that the changes only apply to a branch.

**_all commits are covered by an assignment_**
: This ensures that all changes belong to the Free Software Foundation,
and avoids the possibility that the branch may become contaminated.

**_a branch is focused_**
: A focused branch has a single objective or goal, and does not contain
unnecessary or irrelevant changes. Cleanups, where identified, being
be pushed into the mainline as soon as possible.

**_a branch tracks mainline_**
: This keeps the level of divergence under control. It also keeps the
pressure on developers to push cleanups and other stuff into the
mainline.

**_a branch shall contain the entire GDB module_**
: The GDB module `gdb` should be specified when creating a
branch (branches of individual files should be avoided). @xref{Tags}.

**_a branch shall be branded using `version.in'_**
: The file `gdb/version.in' shall be modified so that it identifies
the branch owner and branch name, e.g.,
`` `6.2.50.20030303_owner_name' `` or `` `6.2 (Owner Name)' ``.

### [Tags](GDB%20Internals.md#apple-krhugmjtga)

@anchor{Tags}

To simplify the identification of GDB branches, the following
branch tagging convention is strongly recommended:

**`owner_name-YYYYMMDD-branchpoint`**
:

**`owner_name-YYYYMMDD-branch`**
: The branch point and corresponding branch tag. YYYYMMDD is the
date that the branch was created. A branch is created using the
sequence: @anchor{experimental branch tags}

```
cvs rtag owner_name-YYYYMMDD-branchpoint gdb
cvs rtag -b -r owner_name-YYYYMMDD-branchpoint \
   owner_name-YYYYMMDD-branch gdb
```

**`owner_name-yyyymmdd-mergepoint`**
: The tagged point, on the mainline, that was used when merging the branch
on yyyymmdd. To merge in all changes since the branch was cut,
use a command sequence like:

```
cvs rtag owner_name-yyyymmdd-mergepoint gdb
cvs update \
   -jowner_name-YYYYMMDD-branchpoint
   -jowner_name-yyyymmdd-mergepoint
```

Similar sequences can be used to just merge in changes since the last
merge.

For further information on CVS, see
@uref{http://www.gnu.org/software/cvs/, Concurrent Versions System}.

---

Go to the [first](Requirements.md), [previous](Porting%20GDB.md), [next](Releasing%20GDB.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
