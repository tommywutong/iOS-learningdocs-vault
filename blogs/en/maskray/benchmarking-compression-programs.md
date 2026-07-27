---
title: Benchmarking compression programs
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2025-08-31-benchmarking-compression-programs'
original_language: en
published: 2025-08-31
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5b84b94ea5e082be'
translated: false
---

> 原文：[Benchmarking compression programs](https://maskray.me/blog/2025-08-31-benchmarking-compression-programs)　·　MaskRay (宋方睿)

[2025-08-31](https://maskray.me/blog/2025-08-31-benchmarking-compression-programs)

# Benchmarking compression programs

tl;dr [https://gist.github.com/MaskRay/74cdaa83c1f44ee105fcebcdff0ba9a7](https://gist.github.com/MaskRay/74cdaa83c1f44ee105fcebcdff0ba9a7) is a single-file Ruby program that downloads and compiles multiple compression utilities, then benchmarks their compression and decompression performance on a specified input file, finally generates a HTML file with scatter charts. Scroll to the end to view example HTML pages.

Compression algorithms can be broadly categorized into three groups based on their typical compression ratio and decompression speed:

- Low ratio, high speed: _lz4, snappy, Oodle Selkie_.
- Medium ratio, medium speed: _zlib, zstd,_brotli_, Oodle Kraken_.
- High ratio, low speed: _LZMA, bzip2, bzip3, bsc, zpaq,_kanzi_, Oodle Leviathan_.

**Low ratio** Codecs in this category prioritize speed above all else. The compression and compression speeds are comparable. They are designed to decompress so quickly that they don't introduce a noticeable delay when reading data from storage like solid-state drives. These codecs typically producing byte-aligned output and often skip the final step of entropy encoding, which, while crucial for high compression, is computationally intensive. They are excellent choices for applications where latency is critical, such as kernel features like zswap.

**Medium ratio** This is the sweet spot for many tasks. The codecs achieve better compression ratio by employing entropy encoding, usually Huffman coding.

_zstd_ has emerged as a clear leader, gaining popularity and effectively supplanting older codecs like the venerable DEFLATE (zlib).

**High ratio** They are designed to squeeze every last bit of redundancy out of the data, often at the cost of significantly longer compression and decompression times, and large memory usage. They are perfect for archival purposes or data distribution where the files are compressed once and decompressed infrequently. Codecs typically have 3 important components:

- Transforms: Codecs typically implement strong transforms to increase redundancy, even very specific ones like branch/call/jump filters for machine code.
- Predication model: This model anticipates the next piece of data based on what has already been processed.
- Entropy encoding: Traditional codecs use arithmetic encoder, which is replaced by the more efficient Range variant of Asymmetric Numeral Systems (rANS).

Some projects apply neural network models, such as Recurrent Neural Network, Long Short-Term Memory, and Transformer, to the predication model. They are usually very slow.

---

This categorization is loose. Many modern programs offer a wide range of compression levels that allow them to essentially span multiple categories. For example, a high-level _zstd_ compression can achieve a ratio comparable to _xz_ (a high-compression codec) by using more RAM and CPU. While _zstd_'s compression speed or ratio is generally lower, its decompression speed is often much faster than that of _xz_.

## Benchmarking

I want to benchmark the single worker performance of a few compression programs:

- _lz4_: Focuses on speed over compression ratio. Memory usage is extremely low. It seems Pareto superior to Google's _Snappy_.
- _zstd_: Gained significant traction and obsoleted many existing codecs. Its LZ77 variant uses three recent match offsets like LZX. For entropy encoding, it employs Huffman coding for literals and 2-way interleaved Finite State Entropy for Huffman weights, literal lengths, match lengths, and offset codes. The large alphabet of literals makes Huffman a good choice, as compressing them with FSE provides little gain for a speed cost. However, other symbols have a small range, making them a sweet spot for FSE. zstd works on multiple streams at the same time to utilize instruction-level parallelism. zstd is supported by the `Accept-Encoding: zstd` HTTP header. Decompression memory usage is very low.
- _brotli_: Uses a combination of LZ77, 2nd order context model, Huffman coding, and static dictionary. The decompression speed is similar to gzip with a higher ratio. At lower levels, its performance is overshadowed by _zstd_. Compared with DEFLATE, it employs a larger sliding window (from 16KiB-16B to 16MiB-16B) and a smaller minimum match length (2 instead of 3). It has a predefined dictionary that works well for web content (but feels less elegant) and supports 120 transforms. _brotli_ is supported by the `Accept-Encoding: br` HTTP header. Decompression memory usage is quite low.
- _bzip3_: Combines BWT, RLE, and LZP and uses arithmetic encoder. Memory usage is large.
- _xz_: LZMA2 with a few filters. The filters must be enabled explicitly.
- lzham: Provides a compression ratio similar to LZMA but with faster decompression. Compression is slightly slower while memory usage is larger. The build system is not well-polished for Linux. I have forked it, fixed `stdint.h` build errors, and installed `lzhamtest`. The command line program `lzhamtest` should really be renamed to `lzham`.
- _zpaq_: Functions as a command-line archiver supporting multiple files. It combines context mixing with arithmetic encoder but operates very slowly.
- _kanzi_: There are a wide variety of transforms and entropy encoders, unusual for a compresion program. For the compression speed of enwik8, it's Pareto superior to _xz_, but decompression is slower. Levels 8 and 9 belong to the PAQ8 family and consume substantial memory.

I'd like to test lzham (not updated for a few years), but I'm having trouble getting it to compile due to a `cstdio` header issue.

Many modern compressors are parallel by default. I have to disable this behavior by using options like `-T1`. Still, _zstd_ uses a worker thread for I/O overlap, but I don't bother with `--single-thread`.

To ensure fairness, each program is built with consistent compiler optimizations, such as `-O3 -march=native`.

Below is a Ruby program that downloads and compiles multiple compression utilities, compresses then decompress a specified input file. It collects performance metrics including execution time, memory usage, and compression ratio, and finally generates an HTML file with scatter charts visualizing the results. The program has several notable features:

- Adding new compressors is easy: just modify `COMPRESSORS`.
- Benchmark results are cached in files named `cache_$basename_$digest.json`, allowing reuse of previous runs for the same input file.
- Adding a new compression level does not invalidate existing benchmark results for other levels.
- The script generates an HTML file with interactive scatter charts. Each compressor is assigned a unique, deterministic color based on a hash of its name (using the `hsl` function in CSS).

The single file Ruby program is available at [https://gist.github.com/MaskRay/74cdaa83c1f44ee105fcebcdff0ba9a7](https://gist.github.com/MaskRay/74cdaa83c1f44ee105fcebcdff0ba9a7)

## Limitation

A single run might not be representative.

Running the executable incurs initialization overhead, which would be amortized in a library setup. However, library setup would make updating libraries more difficult.

## Demo

```sh
ruby bench.rb enwik8
# The first iframe below

ruby bench.rb clang
# The second iframe below
```

Many programs exhibit a stable decompression speed (uncompressed size / decompression time). There is typically a slightly higher decompression speed at higher compression levels. If you think of the compressed content as a form of "byte code", a more highly compressed file means there are fewer bytes for the decompression algorithm to process, resulting in faster decompression. Some programs, like _zpaq_ and _kanzi_, use different algorithms that can result in significantly different decompression speeds.

`xz -9` doesn't use parallelism on the two files under ~100 MiB because their uncompressed size is smaller than the default block size for level 9.

> From `install/include/lzma/container.h`
> 
> For each thread, about 3 * block_size bytes of memory will be allocated. This may change in later liblzma versions. If so, the memory usage will probably be reduced, not increased.
