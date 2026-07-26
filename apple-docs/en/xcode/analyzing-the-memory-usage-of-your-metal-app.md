---
title: Analyzing the memory usage of your Metal app
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/analyzing-the-memory-usage-of-your-metal-app
source_url: 'https://developer.apple.com/documentation/xcode/analyzing-the-memory-usage-of-your-metal-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/analyzing-the-memory-usage-of-your-metal-app.json'
content_hash: 'sha256:f3dd650759c1d31b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md)

# Analyzing the memory usage of your Metal app

<sub>Article</sub>

Keep your app alive in the background by managing its memory footprint.

## Overview

Instruments provides the Game Memory template to help you understand the memory growth in your Metal app. Keeping a small memory footprint allows the system to keep the app alive in the background longer, especially on devices with more constrained memory capacity. For more information, see [Profile and optimize your game’s memory](https://developer.apple.com/videos/play/wwdc2022/10106/).

### Open the Game Memory template

Start the memory analysis from your Xcode project by choosing Product \> Profile, or by pressing Command-I. Alternatively, you can launch Instruments and then select the process from the drop-down list.

In the Template Selection window, select Game Memory.

![A screenshot of the Template Selection window with the Game Memory template selected.](../../../attachments/6ead2ec149cb0e1393b371a0d09a78e4/gputools-instruments-game-memory-choose-template@2x.png)

### Get to know the instruments

- **Allocations** — Analyzes the memory life cycle of a process’s allocated blocks, and can record reference-counting events.
- **Metal Resource Events** — Records Metal GPU resource allocations, such as textures and buffers.
- **VM Tracker** — Tracks the virtual memory space of a process over time, identifying regions by tag and reporting usage statistics.
- **Virtual Memory Trace** — Tracks virtual memory activity per thread.
- **Metal Application** — Records Metal app events.
- **GPU** — Records GPU events.

### Record an Instruments capture

Begin collecting the data by clicking the Record button.

![A screenshot of the Instruments window highlighting the Record button.](../../../attachments/28faaed2513959dd83f9299a96e50b69/gputools-instruments-game-memory-record@2x.png)

Within your app, perform the actions that reproduce the memory problem, and then click the Record button to stop recording.

### Analyze your app’s memory allocations

The Game Memory template shows both memory allocations and memory footprint.

Memory allocations occupy space in the virtual memory address space. When your app allocates memory, these new allocations may not immediately take up space on physical memory. It’s not until your app uses these allocations that they consume physical memory.

The Allocations track provides a detailed view of memory allocations, their sizes, and object reference counts.

> [!note] Note
> The Allocations track doesn’t include Metal resources with private storage mode — only managed and shared storage modes.

![](../../../attachments/a7ef7ee3f0561d17f3d618a01e1d21b1/gputools-instruments-game-memory-allocations@2x.png)

<sub>A screenshot of Instruments with the Allocations track selected. The bottom details pane displays the statistics from the Allocations track.</sub>

The Statistics view in the bottom detail area displays the categories of memory allocations. At the top of the Category column, there are three umbrella categories that summarize all allocations:

- **All Heap & Anonymous VM** — Includes everything.
- **All Heap Allocations** — Includes dynamically allocated buffers that may contain resources.
- **All Anonymous VM** — Includes interesting VM regions that may be dirty. You can also find some Metal-related memory here.

Below them, you can find more detailed categories. Metal resource allocations are in the `VM: IOAccelerator` category, and drawables are in `VM: IOSurface`.

To inspect the individual allocations in a category, click the arrow button next to the category name in the table.

![A screenshot of the details pane displaying the statistics from the Allocations track.](../../../attachments/125f1d944a338303f144905308943203/gputools-instruments-game-memory-allocations-category-button@2x.png)

After selecting a category, you can sort the table by the Size column to find the largest memory allocation during the selected time range.

![A screenshot of the details pane displaying the All Heap Allocations statistics from the Allocations track.](../../../attachments/25af05983a96078c9c5c5762fe92b069/gputools-instruments-game-memory-allocations-all-heap-allocations@2x.png)

You can also select an allocation in the list to view its description and stack trace in the inspector on the right.

### Analyze Metal resource allocations

The Metal Resource Events track displays a history of all Metal-specific resource allocations and deallocations, along with their labels (see [Naming resources and commands](naming-resources-and-commands.md)).

![](../../../attachments/94673e4047864c5e2d256642b4d96451/gputools-instruments-game-memory-metal-resource-events@2x.png)

<sub>A screenshot of Instruments with the Metal Resource Events track selected. The bottom details pane displays the list of resource events.</sub>

The Resource Events view in the bottom detail area lists the resource allocation and deallocation events. It includes events from created or destroyed resources in the selected time range. Not all resources in the list persisted until the end of the time range.

### Analyze your app’s total virtual memory footprint

The Allocations track and the Metal Resource Events track both highlight memory allocations. However, allocations don’t always translate to memory footprint. The VM Tracker track shows the noncompressed and compressed/swapped dirty memory that together make up your app’s memory footprint.

Memory operates on the granularity of pages, and those pages can be either clean or dirty.

- **Clean memory** — Includes memory-mapped files and read-only frameworks.
- **Dirty memory** — Includes heap-allocated memory and written symbols in frameworks.

To conserve the amount of physical memory that your app uses, the system may compress or swap out some dirty pages that your app hasn’t accessed recently.

> [!important] Important
> The system charges your app for any compressed/swapped memory based on its orginal size before compression.

![](../../../attachments/8b246e2860af1db08f3942abbdf92ad3/gputools-instruments-game-memory-vm-tracker@2x.png)

<sub>A screenshot of Instruments with the VM Tracker track selected. The bottom details pane displays a summary of the VM regions.</sub>

The center timeline area graphs the following metrics:

- **Dirty Size** — The amount of noncompressed dirty memory.
- **Swapped Size** — The amount of compressed/swapped dirty memory in its original size before compression.
- **Resident Size** — The amount of resident memory.

The corresponding columns are also available in the Summary view of the bottom detail area. There, you can expand the VM region types. In the mapped file type in the screenshot below, you can see the memory-mapped file of the bistro scene that the Modern Renderer app loaded:

![A screenshot of the details pane displaying a summary of the VM regions highlighting the largest memory-mapped file.](../../../attachments/59da789811e66b333ea3537a55157f5b/gputools-instruments-game-memory-vm-tracker-mapped-file@2x.png)

## See Also

### Graphics

- [Analyzing the performance of your Metal app](analyzing-the-performance-of-your-metal-app.md) — Ensure consistent, smooth rendering by profiling your app’s frame time.
