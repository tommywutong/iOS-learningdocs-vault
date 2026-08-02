---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Foundation_Query_Hardware_Core_CFQueryHardware_h.html
archived_at: '2026-07-18T03:18:12.926177Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Foundation-Query-Hardware-Data-CFQueryHardwareDataSourc.md)[Previous](Sources-Frameworks-Model-Foundation-Query-Hardware-Core-CFQueryHardware.mm.md)

# Sources/Frameworks/Model/Foundation/Query/Hardware/Core/CFQueryHardware.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for querying hardware features.
 */

#ifndef _CORE_FOUNDATION_QUERY_HARDWARE_H_
#define _CORE_FOUNDATION_QUERY_HARDWARE_H_

#import <string>
#import <cmath>

#ifdef __cplusplus

namespace CF
{
    namespace Query
    {
        namespace Frequency
        {
            extern double_t kHertz;
            extern double_t kKiloHertz;
            extern double_t kMegaHertz;
            extern double_t kGigaHetrz;
        };

        class Hardware
        {
        public:
            Hardware(const double_t& frequency = Frequency::kGigaHetrz);

            virtual ~Hardware();

            Hardware(const Hardware& hw);

            Hardware& operator=(const Hardware& hw);

            const size_t&      cores()  const;
            const size_t&      memory() const;
            const double_t&    cpu()    const;
            const std::string& model()  const;

        private:
            std::string  m_Model;
            double_t     mnCPU;
            double_t     mnFreq;
            size_t       mnCores;
            size_t       mnSize;
        }; // Hardware
    } // Query
} // CF

#endif

#endif
```

[Next](Sources-Frameworks-Model-Foundation-Query-Hardware-Data-CFQueryHardwareDataSourc.md)[Previous](Sources-Frameworks-Model-Foundation-Query-Hardware-Core-CFQueryHardware.mm.md)

