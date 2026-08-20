---
title: 'CompressionSample: Compressing Blocks and Streams of Data'
apple_id: TP40016182
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CompressionSample/Listings/CompressionSample_BlockCompression_c.html
archived_at: '2026-07-18T03:04:12.073368Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CompressionSample: Compressing Blocks and Streams of Data](CompressionSample-%20Compressing%20Blocks%20and%20Streams%20of%20Data.md)


[Next](CompressionSample-AAPLViewController.h.md)[Previous](CompressionSample-AAPLAppDelegate.m.md)

# CompressionSample/BlockCompression.c

```c
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides code that performs block compression.
*/

/*
    Example code to compress/encrypt an input file, and then to decrypt/decompress the intermidiate file.
    Input should be identical to output.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "compression.h"
#include <CommonCrypto/CommonCryptor.h>

float doBlockCompression(FILE* fi, FILE* fo, compression_algorithm algorithm)
{
    // Returns the compression ratio.

    // Input buffer: Determine buffer size, allocate, and fill.
    fseek(fi, 0L, SEEK_END);
    size_t src_size = ftell(fi);
    fseek(fi, 0L, SEEK_SET);

    uint8_t *src_buffer = malloc(src_size);
    if (src_buffer == NULL) {
        fprintf(stderr,"error: fail to allocate src buffer (%zu bytes) \n", src_size);
        return 0;
    }

    fread(src_buffer, 1, src_size, fi);

    // Output buffer: Allocate (add extra 4096 bytes).
    size_t dst_size = src_size+4096;
    uint8_t *dst_buffer = malloc(dst_size);
    if (dst_buffer == NULL) {
        fprintf(stderr,"error: fail to allocate dst buffer (%zu bytes) \n", dst_size);
        return 0;
    }

    /*
        When doing both compression and encryption, do compression first.
        Compression may not work well on encrypted data.
    */

    // LZFSE compression.
    dst_size = compression_encode_buffer(dst_buffer, dst_size, src_buffer, src_size, NULL, algorithm);

    // Pad bytes, if needed, for 16-byte/block encryption.
    while (dst_size&15) {
        dst_buffer[dst_size++] = 0;
    }

    float compression_ratio = ((float) src_size)/((float) dst_size);
    printf("compression ratio = %.2f\n", compression_ratio);
    printf("compression ratio = %.2f\n", ((float) src_size)/((float) dst_size));

    if (dst_size >= src_size) {
        fprintf(stderr, "compression ratio < 1, early exit.\n");
        return 1;
    }

    // AES-128 KEY (used for both encryption and decryption).
    const uint8_t AES_KEY[16] = "0123456789abcedf";
    size_t byteProcessed;

    // ECB encryption.
    CCCryptorRef cryptor;
    if (kCCSuccess != CCCryptorCreate(kCCEncrypt, kCCAlgorithmAES, kCCOptionECBMode, AES_KEY, 16, NULL, &cryptor)) {
        fprintf(stderr," error in CCCryptorCreate encrypt\n");
        exit(1);
    }

    if (kCCSuccess != CCCryptorUpdate(cryptor, dst_buffer, dst_size, src_buffer, dst_size, &byteProcessed)) {
        fprintf(stderr,"encrypt update fails.\n");
        exit(2);
    }

    // Write compressed and encrypted output.
    fwrite(src_buffer, 1, dst_size, fo);

    // ECB decryption.
    CCCryptorRef decryptor;
    if (kCCSuccess != CCCryptorCreate(kCCDecrypt, kCCAlgorithmAES, kCCOptionECBMode, AES_KEY, 16, NULL, &decryptor)) {
        fprintf(stderr," error in CCCryptorCreate decrypt\n");
        exit(3);
    }

    if (kCCSuccess != CCCryptorUpdate(decryptor, src_buffer, dst_size, dst_buffer, dst_size, &byteProcessed)) {
        fprintf(stderr, "decrypt update fails.\n");
        exit(4);
    }

    // LZFSE decompression.
    src_size = compression_decode_buffer(src_buffer, src_size, dst_buffer, dst_size, NULL, algorithm);

    // Write decrypted and decompressed output.
    fwrite(src_buffer, 1, src_size, fo);

    // Close files.
    fclose(fi);
    fclose(fo);

    // Free allocated memory.
    free(src_buffer);
    free(dst_buffer);

    return compression_ratio;
}
```

[Next](CompressionSample-AAPLViewController.h.md)[Previous](CompressionSample-AAPLAppDelegate.m.md)

