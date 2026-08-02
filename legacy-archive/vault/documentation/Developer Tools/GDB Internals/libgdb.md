---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_5.html
archived_at: '2026-07-15T07:31:03.864341Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](User%20Interface.md), [next](Symbol%20Handling.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [libgdb](GDB%20Internals.md#apple-krhugmry)

## [libgdb 1.0](GDB%20Internals.md#apple-krhugmrz)

`libgdb` 1.0 was an abortive project of years ago. The theory was
to provide an API to GDB's functionality.

## [libgdb 2.0](GDB%20Internals.md#apple-krhugmzq)

`libgdb` 2.0 is an ongoing effort to update GDB so that is
better able to support graphical and other environments.

Since `libgdb` development is on-going, its architecture is still
evolving. The following components have so far been identified:

- Observer - `gdb-events.h'.
- Builder - `ui-out.h'
- Event Loop - `event-loop.h'
- Library - `gdb.h'

The model that ties these components together is described below.

## [The `libgdb` Model](gdbint_toc.md#apple-krhugmzr)

A client of `libgdb` interacts with the library in two ways.

- As an observer (using `gdb-events') receiving notifications from
  `libgdb` of any internal state changes (break point changes, run
  state, etc).
- As a client querying `libgdb` (using the `ui-out' builder) to
  obtain various status values from GDB.

Since `libgdb` could have multiple clients (e.g. a GUI supporting
the existing GDB CLI), those clients must co-operate when
controlling `libgdb`. In particular, a client must ensure that
`libgdb` is idle (i.e. no other client is using `libgdb`)
before responding to a `gdb-event' by making a query.

## [CLI support](GDB%20Internals.md#apple-krhugmzs)

At present GDB's CLI is very much entangled in with the core of
`libgdb`. Consequently, a client wishing to include the CLI in
their interface needs to carefully co-ordinate its own and the CLI's
requirements.

It is suggested that the client set `libgdb` up to be bi-modal
(alternate between CLI and client query modes). The notes below sketch
out the theory:

- The client registers itself as an observer of `libgdb`.
- The client create and install `cli-out` builder using its own
  versions of the `ui-file` `gdb_stderr`, `gdb_stdtarg` and
  `gdb_stdout` streams.
- The client creates a separate custom `ui-out` builder that is only
  used while making direct queries to `libgdb`.

When the client receives input intended for the CLI, it simply passes it
along. Since the `cli-out` builder is installed by default, all
the CLI output in response to that command is routed (pronounced rooted)
through to the client controlled `gdb_stdout` et. al. streams.
At the same time, the client is kept abreast of internal changes by
virtue of being a `libgdb` observer.

The only restriction on the client is that it must wait until
`libgdb` becomes idle before initiating any queries (using the
client's custom builder).

## [`libgdb` components](gdbint_toc.md#apple-krhugmzt)

### Observer - `gdb-events.h'

`gdb-events' provides the client with a very raw mechanism that can
be used to implement an observer. At present it only allows for one
observer and that observer must, internally, handle the need to delay
the processing of any event notifications until after `libgdb` has
finished the current command.

### Builder - `ui-out.h'

`ui-out' provides the infrastructure necessary for a client to
create a builder. That builder is then passed down to `libgdb`
when doing any queries.

### Event Loop - `event-loop.h'

`event-loop', currently non-re-entrant, provides a simple event
loop. A client would need to either plug its self into this loop or,
implement a new event-loop that GDB would use.

The event-loop will eventually be made re-entrant. This is so that
GDB can better handle the problem of some commands blocking
instead of returning.

### Library - `gdb.h'

`libgdb' is the most obvious component of this system. It provides
the query interface. Each function is parameterized by a `ui-out`
builder. The result of the query is constructed using that builder
before the query function returns.

---

Go to the [first](Requirements.md), [previous](User%20Interface.md), [next](Symbol%20Handling.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
