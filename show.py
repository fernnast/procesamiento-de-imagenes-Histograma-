# Copyright 2025 Dr. Carlos Lopez-Franco.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
import matplotlib.pyplot as plt

def imshow(Im):
    if len(Im.shape) == 3:
        Irgb= cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)
        plt.imshow(Irgb)
    else:
        plt.imshow(Im, cmap='gray')
        
    plt.axis('off')
    plt.show()


