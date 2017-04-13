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

from unittest import TestCase
import heapq
import random

import cyheapq


class CyHeapQTests(TestCase):
    def test_merge(self):
        a = [random.random() for _ in range(1000)]
        b = [random.random() for _ in range(1000)]
        c = [random.random() for _ in range(1000)]

        actual = list(cyheapq.merge(a, b, c))
        expected = list(heapq.merge(a, b, c))
        self.assertEqual(actual, expected)


    def test_nlargest(self):
        a = [random.random() for _ in range(1000)]

        actual = cyheapq.nlargest(10, a)
        expected = heapq.nlargest(10, a)
        self.assertEqual(actual, expected)


    def test_nsmallest(self):
        a = [random.random() for _ in range(1000)]

        actual = cyheapq.nsmallest(10, a)
        expected = heapq.nsmallest(10, a)
        self.assertEqual(actual, expected)
