# Auto generated from authorReference.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-14 15:57
# Schema: authorReference
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/authorReference
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from . core import InformationContentEntity
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/authorReference/')


# Types

# Class references



@dataclass
class AuthorReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/authorReference/AuthorReference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "author reference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/authorReference/AuthorReference")

    corresponding_author: Optional[Union[dict, InformationContentEntity]] = None
    first_name: Optional[Union[dict, InformationContentEntity]] = None
    middle_names: Optional[Union[dict, InformationContentEntity]] = None
    last_name: Optional[Union[dict, InformationContentEntity]] = None
    initials: Optional[Union[dict, InformationContentEntity]] = None
    cross_references: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, InformationContentEntity):
            self.corresponding_author = InformationContentEntity(**self.corresponding_author)

        if self.first_name is not None and not isinstance(self.first_name, InformationContentEntity):
            self.first_name = InformationContentEntity(**self.first_name)

        if self.middle_names is not None and not isinstance(self.middle_names, InformationContentEntity):
            self.middle_names = InformationContentEntity(**self.middle_names)

        if self.last_name is not None and not isinstance(self.last_name, InformationContentEntity):
            self.last_name = InformationContentEntity(**self.last_name)

        if self.initials is not None and not isinstance(self.initials, InformationContentEntity):
            self.initials = InformationContentEntity(**self.initials)

        if self.cross_references is None:
            self.cross_references = []
        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, str) else str(v) for v in self.cross_references]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.corresponding_author = Slot(uri=DEFAULT_.corresponding_author, name="corresponding author", curie=DEFAULT_.curie('corresponding_author'),
                   model_uri=DEFAULT_.corresponding_author, domain=InformationContentEntity, range=Optional[Union[dict, InformationContentEntity]])

slots.first_name = Slot(uri=DEFAULT_.first_name, name="first name", curie=DEFAULT_.curie('first_name'),
                   model_uri=DEFAULT_.first_name, domain=InformationContentEntity, range=Optional[Union[dict, InformationContentEntity]])

slots.middle_names = Slot(uri=DEFAULT_.middle_names, name="middle names", curie=DEFAULT_.curie('middle_names'),
                   model_uri=DEFAULT_.middle_names, domain=InformationContentEntity, range=Optional[Union[dict, InformationContentEntity]])

slots.last_name = Slot(uri=DEFAULT_.last_name, name="last name", curie=DEFAULT_.curie('last_name'),
                   model_uri=DEFAULT_.last_name, domain=InformationContentEntity, range=Optional[Union[dict, InformationContentEntity]])

slots.initials = Slot(uri=DEFAULT_.initials, name="initials", curie=DEFAULT_.curie('initials'),
                   model_uri=DEFAULT_.initials, domain=InformationContentEntity, range=Optional[Union[dict, InformationContentEntity]])
