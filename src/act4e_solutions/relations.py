from typing import Any, TypeVar

import act4e_interfaces as I
from act4e_interfaces import FiniteRelation

E1 = TypeVar("E1")
E2 = TypeVar("E2")
E3 = TypeVar("E3")
E = TypeVar("E")

A = TypeVar("A")
B = TypeVar("B")


class MyFiniteRelationProperties(I.FiniteRelationProperties):
    def is_surjective(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_defined_everywhere(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_injective(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_single_valued(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()


class MyFiniteRelationOperations(I.FiniteRelationOperations):
    def transpose(self, fr: I.FiniteRelation[A, B]) -> I.FiniteRelation[B, A]:
        raise NotImplementedError()


class MyFiniteEndorelationProperties(I.FiniteEndorelationProperties):
    def is_reflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_irreflexive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_transitive(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_symmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_antisymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()

    def is_asymmetric(self, fr: I.FiniteRelation[Any, Any]) -> bool:
        raise NotImplementedError()


class MyFiniteEndorelationOperations(I.FiniteEndorelationOperations):
    def transitive_closure(self, fr: I.FiniteRelation[E, E]) -> I.FiniteRelation[E, E]:
        raise NotImplementedError()


class MyFiniteRelationCompose(I.FiniteRelationCompose):
    def compose(self, fr1: FiniteRelation[E1, E2], fr2: FiniteRelation[E2, E3]) -> I.FiniteRelation[E1, E3]:
        raise NotImplementedError()