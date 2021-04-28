# Auto generated from genomic.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-28 15:35
# Schema: Alliance-Schema-Prototype-Variation
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic
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
from linkml.utils.metamodelcore import URIorCURIE
from linkml_model.types import String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/')


# Types

# Class references
class ChromosomeCurie(URIorCURIE):
    pass


class AssemblyCurie(URIorCURIE):
    pass


@dataclass
class Chromosome(YAMLRoot):
    """
    The ID of the landmark used to establish the coordinate system for the current feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Chromosome")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Chromosome"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Chromosome")

    curie: Union[str, ChromosomeCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is None:
            raise ValueError("curie must be supplied")
        if not isinstance(self.curie, ChromosomeCurie):
            self.curie = ChromosomeCurie(self.curie)

        super().__post_init__(**kwargs)


@dataclass
class Assembly(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Assembly")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Assembly"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Assembly")

    curie: Union[str, AssemblyCurie] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is None:
            raise ValueError("curie must be supplied")
        if not isinstance(self.curie, AssemblyCurie):
            self.curie = AssemblyCurie(self.curie)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.start = Slot(uri=DEFAULT_.start, name="start", curie=DEFAULT_.curie('start'),
                   model_uri=DEFAULT_.start, domain=None, range=Optional[str])

slots.end = Slot(uri=DEFAULT_.end, name="end", curie=DEFAULT_.curie('end'),
                   model_uri=DEFAULT_.end, domain=None, range=Optional[str])

slots.gene_id = Slot(uri=DEFAULT_.gene_id, name="gene_id", curie=DEFAULT_.curie('gene_id'),
                   model_uri=DEFAULT_.gene_id, domain=None, range=str)

slots.chromosome_id = Slot(uri=DEFAULT_.chromosome_id, name="chromosome_id", curie=DEFAULT_.curie('chromosome_id'),
                   model_uri=DEFAULT_.chromosome_id, domain=None, range=str)

slots.transcript_id = Slot(uri=DEFAULT_.transcript_id, name="transcript_id", curie=DEFAULT_.curie('transcript_id'),
                   model_uri=DEFAULT_.transcript_id, domain=None, range=str)

slots.assembly_id = Slot(uri=DEFAULT_.assembly_id, name="assembly_id", curie=DEFAULT_.curie('assembly_id'),
                   model_uri=DEFAULT_.assembly_id, domain=None, range=str)

slots.allele_id = Slot(uri=DEFAULT_.allele_id, name="allele_id", curie=DEFAULT_.curie('allele_id'),
                   model_uri=DEFAULT_.allele_id, domain=None, range=str)

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])
