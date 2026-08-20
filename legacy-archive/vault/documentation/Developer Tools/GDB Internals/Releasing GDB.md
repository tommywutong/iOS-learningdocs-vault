---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_16.html
archived_at: '2026-07-15T07:31:03.749344Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Versions%20and%20Branches.md), [next](Testsuite.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Releasing GDB](GDB%20Internals.md#apple-krhugmjtge)

## [Branch Commit Policy](GDB%20Internals.md#apple-krhugmjtgi)

The branch commit policy is pretty slack. GDB releases 5.0,
5.1 and 5.2 all used the below:

- The `gdb/MAINTAINERS' file still holds.
- Don't fix something on the branch unless/until it is also fixed in the
  trunk. If this isn't possible, mentioning it in the `gdb/PROBLEMS'
  file is better than committing a hack.
- When considering a patch for the branch, suggested criteria include:
  Does it fix a build? Does it fix the sequence `break main; run`
  when debugging a static binary?
- The further a change is from the core of GDB, the less likely
  the change will worry anyone (e.g., target specific code).
- Only post a proposal to change the core of GDB after you've
  sent individual bribes to all the people listed in the
  `MAINTAINERS' file ;-)

_Pragmatics: Provided updates are restricted to non-core
functionality there is little chance that a broken change will be fatal.
This means that changes such as adding a new architectures or (within
reason) support for a new host are considered acceptable._

## [Obsoleting code](GDB%20Internals.md#apple-krhugmjtgm)

Before anything else, poke the other developers (and around the source
code) to see if there is anything that can be removed from GDB
(an old target, an unused file).

Obsolete code is identified by adding an `OBSOLETE` prefix to every
line. Doing this means that it is easy to identify something that has
been obsoleted when greping through the sources.

The process is done in stages -- this is mainly to ensure that the
wider GDB community has a reasonable opportunity to respond.
Remember, everything on the Internet takes a week.

1. Post the proposal on @email{gdb@sources.redhat.com, the GDB mailing
   list} Creating a bug report to track the task's state, is also highly
   recommended.
2. Wait a week or so.
3. Post the proposal on @email{gdb-announce@sources.redhat.com, the GDB
   Announcement mailing list}.
4. Wait a week or so.
5. Go through and edit all relevant files and lines so that they are
   prefixed with the word `OBSOLETE`.
6. Wait until the next GDB version, containing this obsolete code, has been
   released.
7. Remove the obsolete code.

_Maintainer note: While removing old code is regrettable it is
hopefully better for GDB's long term development. Firstly it
helps the developers by removing code that is either no longer relevant
or simply wrong. Secondly since it removes any history associated with
the file (effectively clearing the slate) the developer has a much freer
hand when it comes to fixing broken files._

## [Before the Branch](GDB%20Internals.md#apple-krhugmjtgq)

The most important objective at this stage is to find and fix simple
changes that become a pain to track once the branch is created. For
instance, configuration problems that stop GDB from even
building. If you can't get the problem fixed, document it in the
`gdb/PROBLEMS' file.

### Prompt for `gdb/NEWS'

People always forget. Send a post reminding them but also if you know
something interesting happened add it yourself. The `schedule`
script will mention this in its e-mail.

### Review `gdb/README'

Grab one of the nightly snapshots and then walk through the
`gdb/README' looking for anything that can be improved. The
`schedule` script will mention this in its e-mail.

### Refresh any imported files.

A number of files are taken from external repositories. They include:

- `texinfo/texinfo.tex'
- `config.guess' et. al. (see the top-level `MAINTAINERS'
  file)
- `etc/standards.texi', `etc/make-stds.texi'

### Check the ARI

@uref{http://sources.redhat.com/gdb/ari,,A.R.I.} is an `awk` script
(Awk Regression Index ;-) that checks for a number of errors and coding
conventions. The checks include things like using `malloc` instead
of `xmalloc` and file naming problems. There shouldn't be any
regressions.

### [Review the bug data base](GDB%20Internals.md#apple-krhugmjtgu)

Close anything obviously fixed.

### [Check all cross targets build](GDB%20Internals.md#apple-krhugmjtgy)

The targets are listed in `gdb/MAINTAINERS'.

## [Cut the Branch](GDB%20Internals.md#apple-krhugmjtg4)

### Create the branch

```shell
$  u=5.1
$  v=5.2
$  V=`echo $v | sed 's/\./_/g'`
$  D=`date -u +%Y-%m-%d`
$  echo $u $V $D
5.1 5_2 2002-03-03
$  echo cvs -f -d :ext:sources.redhat.com:/cvs/src rtag \
-D $D-gmt gdb_$V-$D-branchpoint insight+dejagnu
cvs -f -d :ext:sources.redhat.com:/cvs/src rtag
-D 2002-03-03-gmt gdb_5_2-2002-03-03-branchpoint insight+dejagnu
$  ^echo ^^
...
$  echo cvs -f -d :ext:sources.redhat.com:/cvs/src rtag \
-b -r gdb_$V-$D-branchpoint gdb_$V-branch insight+dejagnu
cvs -f -d :ext:sources.redhat.com:/cvs/src rtag \
-b -r gdb_5_2-2002-03-03-branchpoint gdb_5_2-branch insight+dejagnu
$  ^echo ^^
...
$
```

- by using `-D YYYY-MM-DD-gmt` the branch is forced to an exact
  date/time.
- the trunk is first taged so that the branch point can easily be found
- Insight (which includes GDB) and dejagnu are all tagged at the same time
- `version.in' gets bumped to avoid version number conflicts
- the reading of `.cvsrc' is disabled using `-f'

### Update `version.in'

```shell
$  u=5.1
$  v=5.2
$  V=`echo $v | sed 's/\./_/g'`
$  echo $u $v$V
5.1 5_2
$  cd /tmp
$  echo cvs -f -d :ext:sources.redhat.com:/cvs/src co \
-r gdb_$V-branch src/gdb/version.in
cvs -f -d :ext:sources.redhat.com:/cvs/src co
 -r gdb_5_2-branch src/gdb/version.in
$  ^echo ^^
U src/gdb/version.in
$  cd src/gdb
$  echo $u.90-0000-00-00-cvs > version.in
$  cat version.in
5.1.90-0000-00-00-cvs
$  cvs -f commit version.in
```

- `0000-00-00' is used as a date to pump prime the version.in update
  mechanism
- `.90' and the previous branch version are used as fairly arbitrary
  initial branch version number

### Update the web and news pages

Something?

### Tweak cron to track the new branch

The file `gdbadmin/cron/crontab' contains gdbadmin's cron table.
This file needs to be updated so that:

- a daily timestamp is added to the file `version.in'
- the new branch is included in the snapshot process

See the file `gdbadmin/cron/README' for how to install the updated
cron table.

The file `gdbadmin/ss/README' should also be reviewed to reflect
any changes. That file is copied to both the branch/ and current/
snapshot directories.

### Update the NEWS and README files

The `NEWS' file needs to be updated so that on the branch it refers
to _changes in the current release_ while on the trunk it also
refers to _changes since the current release_.

The `README' file needs to be updated so that it refers to the
current release.

### Post the branch info

Send an announcement to the mailing lists:

- @email{gdb-announce@sources.redhat.com, GDB Announcement mailing list}
- @email{gdb@sources.redhat.com, GDB Discsussion mailing list} and
  @email{gdb-testers@sources.redhat.com, GDB Discsussion mailing list}

_Pragmatics: The branch creation is sent to the announce list to
ensure that people people not subscribed to the higher volume discussion
list are alerted._

The announcement should include:

- the branch tag
- how to check out the branch using CVS
- the date/number of weeks until the release
- the branch commit policy
  still holds.

## [Stabilize the branch](GDB%20Internals.md#apple-krhugmjtha)

Something goes here.

## [Create a Release](GDB%20Internals.md#apple-krhugmjthe)

The process of creating and then making available a release is broken
down into a number of stages. The first part addresses the technical
process of creating a releasable tar ball. The later stages address the
process of releasing that tar ball.

When making a release candidate just the first section is needed.

### [Create a release candidate](GDB%20Internals.md#apple-krhugmjuga)

The objective at this stage is to create a set of tar balls that can be
made available as a formal release (or as a less formal release
candidate).

#### Freeze the branch

Send out an e-mail notifying everyone that the branch is frozen to
@email{gdb-patches@sources.redhat.com}.

#### Establish a few defaults.

```shell
$  b=gdb_5_2-branch
$  v=5.2
$  t=/sourceware/snapshot-tmp/gdbadmin-tmp
$  echo $t/$b/$v
/sourceware/snapshot-tmp/gdbadmin-tmp/gdb_5_2-branch/5.2
$  mkdir -p $t/$b/$v
$  cd $t/$b/$v
$  pwd
/sourceware/snapshot-tmp/gdbadmin-tmp/gdb_5_2-branch/5.2
$  which autoconf
/home/gdbadmin/bin/autoconf
$
```

Notes:

- Check the `autoconf` version carefully. You want to be using the
  version taken from the `binutils' snapshot directory, which can be
  found at @uref{ftp://sources.redhat.com/pub/binutils/}. It is very
  unlikely that a system installed version of `autoconf` (e.g.,
  `/usr/bin/autoconf') is correct.

#### Check out the relevant modules:

```
$  for m in gdb insight dejagnu
do
( mkdir -p $m && cd $m && cvs -q -f -d /cvs/src co -P -r $b $m )
done
$
```

Note:

- The reading of `.cvsrc' is disabled (`-f') so that there isn't
  any confusion between what is written here and what your local
  `cvs` really does.

#### Update relevant files.

**`gdb/NEWS'**
: Major releases get their comments added as part of the mainline. Minor
releases should probably mention any significant bugs that were fixed.
Don't forget to include the `ChangeLog' entry.

```shell
$  emacs gdb/src/gdb/NEWS
...
c-x 4 a
...
c-x c-s c-x c-c
$  cp gdb/src/gdb/NEWS insight/src/gdb/NEWS
$  cp gdb/src/gdb/ChangeLog insight/src/gdb/ChangeLog
```

**`gdb/README'**
: You'll need to update:

- the version
- the update date
- who did it

```shell
$  emacs gdb/src/gdb/README
...
c-x 4 a
...
c-x c-s c-x c-c
$  cp gdb/src/gdb/README insight/src/gdb/README
$  cp gdb/src/gdb/ChangeLog insight/src/gdb/ChangeLog
```

_Maintainer note: Hopefully the `README' file was reviewed
before the initial branch was cut so just a simple substitute is needed
to get it updated._
_Maintainer note: Other projects generate `README' and
`INSTALL' from the core documentation. This might be worth
pursuing._

**`gdb/version.in'**
: ```
$  echo $v > gdb/src/gdb/version.in
$  cat gdb/src/gdb/version.in
5.2
$  emacs gdb/src/gdb/version.in
...
c-x 4 a
... Bump to version ...
c-x c-s c-x c-c
$  cp gdb/src/gdb/version.in insight/src/gdb/version.in
$  cp gdb/src/gdb/ChangeLog insight/src/gdb/ChangeLog
```

**`dejagnu/src/dejagnu/configure.in'**
: Dejagnu is more complicated. The version number is a parameter to
`AM_INIT_AUTOMAKE`. Tweak it to read something like gdb-5.1.91.
Don't forget to re-generate `configure'.
Don't forget to include a `ChangeLog' entry.

```
$  emacs dejagnu/src/dejagnu/configure.in
...
c-x 4 a
...
c-x c-s c-x c-c
$  ( cd  dejagnu/src/dejagnu && autoconf )
```

#### Do the dirty work

This is identical to the process used to create the daily snapshot.

```
$  for m in gdb insight
do
( cd $m/src && gmake -f src-release $m.tar )
done
$  ( m=dejagnu; cd $m/src && gmake -f src-release $m.tar.bz2 )
```

If the top level source directory does not have `src-release'
(GDB version 5.3.1 or earlier), try these commands instead:

```
$  for m in gdb insight
do
( cd $m/src && gmake -f Makefile.in $m.tar )
done
$  ( m=dejagnu; cd $m/src && gmake -f Makefile.in $m.tar.bz2 )
```

#### Check the source files

You're looking for files that have mysteriously disappeared.
`distclean` has the habit of deleting files it shouldn't. Watch out
for the `version.in' update `cronjob`.

```
$  ( cd gdb/src && cvs -f -q -n update )
M djunpack.bat
? gdb-5.1.91.tar
? proto-toplev
... lots of generated files ...
M gdb/ChangeLog
M gdb/NEWS
M gdb/README
M gdb/version.in
... lots of generated files ...
$
```

_Don't worry about the `gdb.info-??' or
`gdb/p-exp.tab.c'. They were generated (and yes `gdb.info-1'
was also generated only something strange with CVS means that they
didn't get supressed). Fixing it would be nice though._

#### Create compressed versions of the release

```
$  cp */src/*.tar .
$  cp */src/*.bz2 .
$  ls -F
dejagnu/ dejagnu-gdb-5.2.tar.bz2 gdb/ gdb-5.2.tar insight/ insight-5.2.tar
$  for m in gdb insight
do
bzip2 -v -9 -c $m-$v.tar > $m-$v.tar.bz2
gzip -v -9 -c $m-$v.tar > $m-$v.tar.gz
done
$
```

Note:

- A pipe such as `bunzip2 < xxx.bz2 | gzip -9 > xxx.gz` is not since,
  in that mode, `gzip` does not know the name of the file and, hence,
  can not include it in the compressed file. This is also why the release
  process runs `tar` and `bzip2` as separate passes.

### <a id="apple-kncugmjuge"></a>[Sanity check the tar ball](gdbint_toc.md#apple-krhugmjuge)

Pick a popular machine (Solaris/PPC?) and try the build on that.

```
$  bunzip2 < gdb-5.2.tar.bz2 | tar xpf -
$  cd gdb-5.2
$  ./configure
$  make
...
$  ./gdb/gdb ./gdb/gdb
GNU gdb 5.2
...
(gdb)  b main
Breakpoint 1 at 0x80732bc: file main.c, line 734.
(gdb)  run
Starting program: /tmp/gdb-5.2/gdb/gdb

Breakpoint 1, main (argc=1, argv=0xbffff8b4) at main.c:734
734       catch_errors (captured_main, &args, "", RETURN_MASK_ALL);
(gdb)  print args
$1 = {argc = 136426532, argv = 0x821b7f0}
(gdb)
```

### <a id="apple-kncugmjugi"></a>[Make a release candidate available](gdbint_toc.md#apple-krhugmjugi)

If this is a release candidate then the only remaining steps are:

1. Commit `version.in' and `ChangeLog'
2. Tweak `version.in' (and `ChangeLog' to read
   L.M.N-0000-00-00-cvs so that the version update
   process can restart.
3. Make the release candidate available in
   @uref{ftp://sources.redhat.com/pub/gdb/snapshots/branch}
4. Notify the relevant mailing lists ( @email{gdb@sources.redhat.com} and
   @email{gdb-testers@sources.redhat.com} that the candidate is available.

### <a id="apple-kncugmjugm"></a>[Make a formal release available](gdbint_toc.md#apple-krhugmjugm)

(And you thought all that was required was to post an e-mail.)

#### Install on sware

Copy the new files to both the release and the old release directory:

```
$  cp *.bz2 *.gz ~ftp/pub/gdb/old-releases/
$  cp *.bz2 *.gz ~ftp/pub/gdb/releases
```

Clean up the releases directory so that only the most recent releases
are available (e.g. keep 5.2 and 5.2.1 but remove 5.1):

```
$  cd ~ftp/pub/gdb/releases
$  rm ...
```

Update the file `README' and `.message' in the releases
directory:

```
$  vi README
...
$  rm -f .message
$  ln README .message
```

#### Update the web pages.

**`htdocs/download/ANNOUNCEMENT'**
: This file, which is posted as the official announcement, includes:

- General announcement
- News. If making an M.N.1 release, retain the news from
  earlier M.N release.
- Errata

**`htdocs/index.html'**
:

**`htdocs/news/index.html'**
:

**`htdocs/download/index.html'**
: These files include:

- announcement of the most recent release
- news entry (remember to update both the top level and the news directory).

These pages also need to be regenerate using `index.sh`.

**`download/onlinedocs/'**
: You need to find the magic command that is used to generate the online
docs from the `.tar.bz2'. The best way is to look in the output
from one of the nightly `cron` jobs and then just edit accordingly.
Something like:

```
$  ~/ss/update-web-docs \
 ~ftp/pub/gdb/releases/gdb-5.2.tar.bz2 \
 $PWD/www \
 /www/sourceware/htdocs/gdb/download/onlinedocs \
 gdb
```

**`download/ari/'**
: Just like the online documentation. Something like:

```
$  /bin/sh ~/ss/update-web-ari \
 ~ftp/pub/gdb/releases/gdb-5.2.tar.bz2 \
 $PWD/www \
 /www/sourceware/htdocs/gdb/download/ari \
 gdb
```

#### Shadow the pages onto gnu

Something goes here.

#### Install the GDB tar ball on GNU

At the time of writing, the GNU machine was `gnudist.gnu.org` in
`~ftp/gnu/gdb'.

#### Make the `ANNOUNCEMENT'

Post the `ANNOUNCEMENT' file you created above to:

- @email{gdb-announce@sources.redhat.com, GDB Announcement mailing list}
- @email{info-gnu@gnu.org, General GNU Announcement list} (but delay it a
  day or so to let things get out)
- @email{bug-gdb@gnu.org, GDB Bug Report mailing list}

### <a id="apple-kncugmjugq"></a>[Cleanup](gdbint_toc.md#apple-krhugmjugq)

The release is out but you're still not finished.

#### Commit outstanding changes

In particular you'll need to commit any changes to:

- `gdb/ChangeLog'
- `gdb/version.in'
- `gdb/NEWS'
- `gdb/README'

#### Tag the release

Something like:

```
$  d=`date -u +%Y-%m-%d`
$  echo $d
2002-01-24
$  ( cd insight/src/gdb && cvs -f -q update )
$  ( cd insight/src && cvs -f -q tag gdb_5_2-$d-release )
```

Insight is used since that contains more of the release than
GDB (`dejagnu` doesn't get tagged but I think we can live
with that).

#### Mention the release on the trunk

Just put something in the `ChangeLog' so that the trunk also
indicates when the release was made.

#### Restart `gdb/version.in'

If `gdb/version.in' does not contain an ISO date such as
`2002-01-24` then the daily `cronjob` won't update it. Having
committed all the release changes it can be set to
`5.2.0_0000-00-00-cvs' which will restart things (yes the `_`
is important - it affects the snapshot process).

Don't forget the `ChangeLog'.

#### Merge into trunk

The files committed to the branch may also need changes merged into the
trunk.

#### Revise the release schedule

Post a revised release schedule to @email{gdb@sources.redhat.com, GDB
Discussion List} with an updated announcement. The schedule can be
generated by running:

```
$  ~/ss/schedule `date +%s` schedule
```

The first parameter is approximate date/time in seconds (from the epoch)
of the most recent release.

Also update the schedule `cronjob`.

## <a id="apple-kncugmjugu"></a>[Post release](gdbint_toc.md#apple-krhugmjugu)

Remove any `OBSOLETE` code.

---

Go to the [first](gdbint_1.md), [previous](gdbint_15.md), [next](gdbint_17.md), [last](gdbint_20.md) section, [table of contents](gdbint_toc.md).
