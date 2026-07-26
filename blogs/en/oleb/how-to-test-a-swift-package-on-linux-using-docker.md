---
title: How to test a Swift package on Linux using Docker
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/03/testing-swift-packages-on-linux/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6ac88151a1353ee8'
translated: false
---

> 原文：[How to test a Swift package on Linux using Docker](https://oleb.net/blog/2017/03/testing-swift-packages-on-linux/)　·　Ole Begemann

# How to test a Swift package on Linux using Docker

**Update:** I wrote an update for this article in February 2020: [Testing Swift packages on Linux using Docker](https://oleb.net/2020/swift-docker-linux/).

[Speaking of testing on Linux](https://oleb.net/blog/2017/03/keeping-xctest-in-sync/), how _do you_ test your Swift package on Linux when your development machine is a Mac? Here’s a quick way to set up a Linux testing environment using [Docker](https://www.docker.com/what-docker) containers. I’m assuming for the following that you have an existing project that works with the [Swift Package Manager](https://swift.org/package-manager/), i.e. you can run `swift build` and `swift test` from the project directory on your Mac.

Follow these steps:

1. **Install [Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac).**
2. **Create a file named `Dockerfile`** in the root directory of your project with these contents:

  ```
  FROM swift:3.1

  WORKDIR /package

  COPY . ./

  RUN swift package fetch --enable-prefetching
  RUN swift package clean # swift build --clean for Swift 3.0
  CMD swift test --parallel
  ```

  The [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is a recipe for building an _image_. The image then forms the base from which we later create the _container_ that will run the tests.

  The `FROM swift:3.1` line sets the base image from which we derive our own image. We use the [“official” Swift image](https://hub.docker.com/r/library/swift/)^[1](#fn:official) in Docker’s public image repository. It’s a standard [Ubuntu](https://www.ubuntu.com) that has the Swift toolchain installed. You can use different tags (the part behind the colon) to select a specific Swift version, or `swift:latest` for the latest version.

  The subsequent lines create a working directory in the image and copy the contents of the project directory from the host (your machine) to the image. If you place your `Dockerfile` in a different directory than your project root, you’ll have to modify the paths in the `COPY . ./` line.

  We then run `swift package fetch` and `swift package clean` to fetch our package’s dependencies and create a clean slate for the build. Fetching the dependencies again is not strictly necessary as they also get copied over from the host, but it’s good practice.

  The last line, `CMD swift test`, specifies the command we want to run when we run the container. In our case, we build the package and run the tests.

  (`swift package clean` requires Swift 3.1 or later. Use `swift build --clean` for Swift 3.0 compatibility. The `--enable-prefetching` and `--parallel` flags are also new in Swift 3.1. You can just leave them out if you want to support Swift 3.0.)
3. **Create another file named `.dockerignore`** in your project directory with these contents:

  ```
  .git/
  .build/
  !.build/checkouts/
  !.build/repositories/
  !.build/workspace-state.json
  ```

  [`.dockerignore`](https://docs.docker.com/engine/reference/builder/#dockerignore-file) works like [`.gitignore`](https://git-scm.com/docs/gitignore). It allows you to exclude certain paths on your host from being copied to the image. We specify the Git directory and the package manager’s build artifacts path because the build products produced on macOS aren’t compatible with Linux. This isn’t strictly necessary because the `RUN swift package clean` command in the `Dockerfile` would delete these anyway.

  The lines starting with `!` exempt paths from the exclusion where the package manager stores the fetched dependencies. This makes building the image faster in the common case because libraries that the host has already fetched don’t have to be downloaded again.
4. **Build the image** by running the following command. Give your image a name of your choice. Mine is called `bananakit`:

  ```
  $ docker build --tag bananakit .
  ...
  Successfully built 2de5f0463f8e
  ```

  This will download the base image from Docker Hub (if necessary) and execute the steps in the `Dockerfile` one by one. After the build finished, you should be able to list your new image with `docker images`.
5. **Now you can create and run a container based on the image:**

  ```
  $ docker run --rm bananakit
  Compile Swift Module 'BananaKit' (1 sources)
  Compile Swift Module 'BananaKitTests' (1 sources)
  Linking ./.build/debug/BananaKitPackageTests.xctest
  Test Suite 'All tests' started at 11:23:44.463
  ...
  Test Suite 'All tests' passed at 11:23:44.464
    Executed 3 tests, with 0 failures (0 unexpected) in 0.0 (0.0) seconds
  ```

  The `--rm` flag tells Docker to automatically delete the container after running it once, which is usually what you want if you just want to check if your tests pass.

Now, every time you change your code and want to run the tests on Linux again, repeat the last two steps: rebuild the image and run the container. Building the image sounds like a time-consuming process but it’s usually very fast because Docker can cache a lot of stuff.

# Alternative 1: swiftenv

What if the “official” Swift image doesn’t work for you, e.g. because it doesn’t support the Swift version you need? Take a look a [Kyle Fuller’s](https://fuller.li) excellent [swiftenv](https://swiftenv.fuller.li), a command line tool for installing any Swift version or [snapshot](https://swift.org/download/#snapshots) you want.

Conveniently, Kyle also provides a [Docker image for swiftenv](https://swiftenv.fuller.li/en/latest/integrations/docker.html) that you can use as a base image. For example, if you want to test your code with a specific Swift snapshot, you can start your `Dockerfile` like this:

```
FROM kylef/swiftenv

RUN swiftenv install DEVELOPMENT-SNAPSHOT-2017-03-30-a
RUN swift --version

WORKDIR /package
...
```

# Alternative 2: Sharing the current directory between host and container

The `Dockerfile` shown above _copies_ the contents of the current directory to the Docker image during image creation. That’s why you have to rerun `docker build` every time you modify any file in your package.

An alternative is to have the host _share_ the directory with the container while the container runs. Both host and container have read-write access to the shared directory and any changes either side makes are immediately visible to both.

You don’t need to build an image at all in this case — the entire customization can be specified in the `docker run` command. So feel free to delete `Dockerfile` and `.dockerignore` and use this command to run the container:

```
$ docker run --rm \
    --volume "$(pwd):/package" \
    --workdir "/package" \
    swift:3.1 \
    /bin/bash -c \
    "swift package fetch && swift test --build-path ./.build/linux"
```

This tells Docker to:

- run a container based on the `swift:3.1` image,
- delete the container when it exits (`--rm`),
- map the current directory on the host to `/package` in the container (`--volume "$(pwd):/package"`),
- change into the `/package` directory in the container (`--workdir "/package"`),
- and execute a Bash shell inside the container, telling the shell to run the command `swift package fetch && swift test ...` and exit.

Note the `--build-path ./.build/linux` parameter we’re passing to `swift test`: now that host and container share the same directory, we have to tell SwiftPM to use a custom location for the Linux build products to avoid conflicts with the binaries built for macOS.

This `docker run` invocation runs the specified command and exits. If you want to interact with the container, you can use the same technique to open a terminal session on the container:

```
$ docker run --rm \
    --interactive \
    --tty \
    --volume "$(pwd):/package" \
    --workdir "/package" \
    swift:3.1
```

1. “Official” as in “endorsed by Docker on Docker Hub”. The image is not being maintained by Apple or the Swift team. [↩︎](#fnref:official)
