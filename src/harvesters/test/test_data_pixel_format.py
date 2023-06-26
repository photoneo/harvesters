#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2023 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Standard library imports
import unittest

# Local application/library specific imports
from harvesters.core import Component2DImage
from harvesters.util.pfnc import Data8, Data8s, Data16, Data16s, Data32, Data32s, Data32f, Data64, Data64s, Data64f


class TestDataFormats(unittest.TestCase):
    _height = 1
    _range = range(0, 3, 1)

    def test_data8(self):
        proxies = [Data8, Data8s]
        expected_bytes = [
            [1, 1],  # 1 x 1
            [2, 2],  # 2 x 1
            [3, 3],  # 3 x 1
        ]
        for i in self._range:
            for j, proxy in enumerate(proxies):
                self.assertEqual(
                    expected_bytes[i][j],
                    Component2DImage._get_nr_bytes(
                        pf_proxy=proxy(), width=i + 1, height=self._height
                    )
                )


    def test_data16(self):
        proxies = [Data16, Data16s]
        expected_bytes = [
            [2, 2],  # 1 x 1
            [4, 4],  # 2 x 1
            [6, 6],  # 3 x 1
        ]
        for i in self._range:
            for j, proxy in enumerate(proxies):
                self.assertEqual(
                    expected_bytes[i][j],
                    Component2DImage._get_nr_bytes(
                        pf_proxy=proxy(), width=i + 1, height=self._height
                    )
                )


    def test_data32(self):
        proxies = [Data32, Data32s, Data32f]
        expected_bytes = [
            [4, 4, 4],  # 1 x 1
            [8, 8, 8],  # 2 x 1
            [12, 12, 12],  # 3 x 1
        ]
        for i in self._range:
            for j, proxy in enumerate(proxies):
                self.assertEqual(
                    expected_bytes[i][j],
                    Component2DImage._get_nr_bytes(
                        pf_proxy=proxy(), width=i + 1, height=self._height
                    )
                )


    def test_data64(self):
        proxies = [Data64, Data64s, Data64f]
        expected_bytes = [
            [8, 8, 8],  # 1 x 1
            [16, 16, 16],  # 2 x 1
            [24, 24, 24],  # 3 x 1
        ]
        for i in self._range:
            for j, proxy in enumerate(proxies):
                self.assertEqual(
                    expected_bytes[i][j],
                    Component2DImage._get_nr_bytes(
                        pf_proxy=proxy(), width=i + 1, height=self._height
                    )
                )


if __name__ == '__main__':
    unittest.main()
