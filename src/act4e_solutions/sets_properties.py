from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

__all__ = ["MyMakeSetUnion", "MyMakeSetIntersection", "MyFiniteSetProperties"]

X = TypeVar("X")


class MyFiniteSetProperties(I.FiniteSetProperties):
    def is_subset(self, a: I.FiniteSet[X], b: I.FiniteSet[X]) -> bool:
        raise NotImplementedError()


class MyMakeSetUnion(I.MakeSetUnion):
    @overload
    def union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetUnion[X, Any]:
        ...

    @overload
    def union(self, components: Sequence[I.EnumerableSet[X]]) -> I.EnumerableSetUnion[X, Any]:
        ...

    def union(self, components: Sequence[I.Setoid[X]]) -> I.SetUnion[X, Any]:
        raise NotImplementedError()


class MyMakeSetIntersection(I.MakeSetIntersection):
    def intersection(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSet[X]:
        raise NotImplementedError()
