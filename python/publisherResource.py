# Auto generated from publisherResource.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-14 15:57
# Schema: publisherResource
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/publisherResource
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
from linkml.utils.metamodelcore import XSDDate
from linkml_model.types import Date, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/publisherResource/')


# Types

# Class references



@dataclass
class PublisherResource(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/publisherResource/PublisherResource")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "publisher resource"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/publisherResource/PublisherResource")

    first_name: Optional[Union[dict, InformationContentEntity]] = None
    middle_names: Optional[Union[dict, InformationContentEntity]] = None
    last_name: Optional[Union[dict, InformationContentEntity]] = None
    initials: Optional[Union[dict, InformationContentEntity]] = None
    cross_references: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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


