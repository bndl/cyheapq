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
import sys

import cyheapq


class CyHeapQTests(TestCase):
    def check_merge(self, **kwargs):
        a = sorted((random.random() for _ in range(10)), **kwargs)
        b = sorted((random.random() for _ in range(10)), **kwargs)
        c = sorted((random.random() for _ in range(10)), **kwargs)

        for lists in ((a,), (a, b), (a, b, c,)):
            actual = list(cyheapq.merge(*lists, **kwargs))
            expected = list(heapq.merge(*lists, **kwargs))
            self.assertEqual(actual, expected)

    def test_merge(self):
        self.check_merge()
        if sys.version_info >= (3,5):
            self.check_merge(reverse=True)
            self.check_merge(key=lambda i:-i)
            self.check_merge(key=lambda i:-i, reverse=True)

    def check_take(self, taker, n, key=None):
        a = [random.random() for _ in range(12)]
        actual = getattr(cyheapq, taker)(10, a, key=key)
        expected = getattr(heapq, taker)(10, a, key=key)
        self.assertEqual(actual, expected)

    def test_nlargest(self):
        self.check_take('nlargest', 10)
        self.check_take('nlargest', 10, key=lambda i:-i)

    def test_nsmallest(self):
        self.check_take('nsmallest', 10)
        self.check_take('nsmallest', 10, key=lambda i:-i)
