# Auto generated from variation.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-21 15:50
# Schema: Alliance-Schema-Prototype-Variation
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/variation
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
from . core import AlleleId, BiologicalSequence, GeneId, NamedThing, NamedThingId, TranscriptId
from . crossReference import CrossReferenceCrossReferenceId
from . reference import ReferenceId
from linkml.utils.metamodelcore import URIorCURIE, XSDDate
from linkml_model.types import Date, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/variation/')


# Types

# Class references
class VariantId(NamedThingId):
    pass


@dataclass
class Variant(NamedThing):
    """
    Variant class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variation/Variant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "variant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variation/Variant")

    id: Union[str, VariantId] = None
    hgvs_nomenclature: Optional[str] = None
    genomic_reference_sequence: Optional[Union[str, BiologicalSequence]] = None
    genomic_variant_sequence: Optional[Union[str, BiologicalSequence]] = None
    padding_left: Optional[Union[str, BiologicalSequence]] = None
    padding_right: Optional[Union[str, BiologicalSequence]] = None
    date_produced: Optional[Union[str, XSDDate]] = None
    release: Optional[str] = None
    data_provider: Optional[Union[str, List[str]]] = empty_list()
    is_variant_of_gene: Optional[Union[str, GeneId]] = None
    is_variant_of_transcript: Optional[Union[str, TranscriptId]] = None
    is_variant_of_allele: Optional[Union[str, AlleleId]] = None
    synonyms: Optional[str] = None
    type: Optional[Union[str, URIorCURIE]] = None
    references: Optional[Union[Union[str, ReferenceId], List[Union[str, ReferenceId]]]] = empty_list()
    note: Optional[str] = None
    protein_sequence: Optional[Union[str, BiologicalSequence]] = None
    cross_references: Optional[Union[Union[str, CrossReferenceCrossReferenceId], List[Union[str, CrossReferenceCrossReferenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantId):
            self.id = VariantId(self.id)

        if self.hgvs_nomenclature is not None and not isinstance(self.hgvs_nomenclature, str):
            self.hgvs_nomenclature = str(self.hgvs_nomenclature)

        if self.genomic_reference_sequence is not None and not isinstance(self.genomic_reference_sequence, BiologicalSequence):
            self.genomic_reference_sequence = BiologicalSequence(self.genomic_reference_sequence)

        if self.genomic_variant_sequence is not None and not isinstance(self.genomic_variant_sequence, BiologicalSequence):
            self.genomic_variant_sequence = BiologicalSequence(self.genomic_variant_sequence)

        if self.padding_left is not None and not isinstance(self.padding_left, BiologicalSequence):
            self.padding_left = BiologicalSequence(self.padding_left)

        if self.padding_right is not None and not isinstance(self.padding_right, BiologicalSequence):
            self.padding_right = BiologicalSequence(self.padding_right)

        if self.date_produced is not None and not isinstance(self.date_produced, XSDDate):
            self.date_produced = XSDDate(self.date_produced)

        if self.release is not None and not isinstance(self.release, str):
            self.release = str(self.release)

        if self.data_provider is None:
            self.data_provider = []
        if not isinstance(self.data_provider, list):
            self.data_provider = [self.data_provider]
        self.data_provider = [v if isinstance(v, str) else str(v) for v in self.data_provider]

        if self.is_variant_of_gene is not None and not isinstance(self.is_variant_of_gene, GeneId):
            self.is_variant_of_gene = GeneId(self.is_variant_of_gene)

        if self.is_variant_of_transcript is not None and not isinstance(self.is_variant_of_transcript, TranscriptId):
            self.is_variant_of_transcript = TranscriptId(self.is_variant_of_transcript)

        if self.is_variant_of_allele is not None and not isinstance(self.is_variant_of_allele, AlleleId):
            self.is_variant_of_allele = AlleleId(self.is_variant_of_allele)

        if self.synonyms is not None and not isinstance(self.synonyms, str):
            self.synonyms = str(self.synonyms)

        if self.type is not None and not isinstance(self.type, URIorCURIE):
            self.type = URIorCURIE(self.type)

        if self.references is None:
            self.references = []
        if not isinstance(self.references, list):
            self.references = [self.references]
        self.references = [v if isinstance(v, ReferenceId) else ReferenceId(v) for v in self.references]

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        if self.protein_sequence is not None and not isinstance(self.protein_sequence, BiologicalSequence):
            self.protein_sequence = BiologicalSequence(self.protein_sequence)

        if self.cross_references is None:
            self.cross_references = []
        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, CrossReferenceCrossReferenceId) else CrossReferenceCrossReferenceId(v) for v in self.cross_references]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.note = Slot(uri=DEFAULT_.note, name="note", curie=DEFAULT_.curie('note'),
                   model_uri=DEFAULT_.note, domain=None, range=Optional[str])

slots.date_produced = Slot(uri=DEFAULT_.date_produced, name="date produced", curie=DEFAULT_.curie('date_produced'),
                   model_uri=DEFAULT_.date_produced, domain=Variant, range=Optional[Union[str, XSDDate]])

slots.hgvs_nomenclature = Slot(uri=DEFAULT_.hgvs_nomenclature, name="hgvs nomenclature", curie=DEFAULT_.curie('hgvs_nomenclature'),
                   model_uri=DEFAULT_.hgvs_nomenclature, domain=Variant, range=Optional[str])

slots.genomic_reference_sequence = Slot(uri=DEFAULT_.genomic_reference_sequence, name="genomic reference sequence", curie=DEFAULT_.curie('genomic_reference_sequence'),
                   model_uri=DEFAULT_.genomic_reference_sequence, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.genomic_variant_sequence = Slot(uri=DEFAULT_.genomic_variant_sequence, name="genomic variant sequence", curie=DEFAULT_.curie('genomic_variant_sequence'),
                   model_uri=DEFAULT_.genomic_variant_sequence, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.padding_left = Slot(uri=DEFAULT_.padding_left, name="padding left", curie=DEFAULT_.curie('padding_left'),
                   model_uri=DEFAULT_.padding_left, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.padding_right = Slot(uri=DEFAULT_.padding_right, name="padding right", curie=DEFAULT_.curie('padding_right'),
                   model_uri=DEFAULT_.padding_right, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.protein_sequence = Slot(uri=DEFAULT_.protein_sequence, name="protein sequence", curie=DEFAULT_.curie('protein_sequence'),
                   model_uri=DEFAULT_.protein_sequence, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.is_variant_of_gene = Slot(uri=DEFAULT_.is_variant_of_gene, name="is variant of gene", curie=DEFAULT_.curie('is_variant_of_gene'),
                   model_uri=DEFAULT_.is_variant_of_gene, domain=Variant, range=Optional[Union[str, GeneId]])

slots.is_variant_of_transcript = Slot(uri=DEFAULT_.is_variant_of_transcript, name="is variant of transcript", curie=DEFAULT_.curie('is_variant_of_transcript'),
                   model_uri=DEFAULT_.is_variant_of_transcript, domain=Variant, range=Optional[Union[str, TranscriptId]])

slots.is_variant_of_allele = Slot(uri=DEFAULT_.is_variant_of_allele, name="is variant of allele", curie=DEFAULT_.curie('is_variant_of_allele'),
                   model_uri=DEFAULT_.is_variant_of_allele, domain=Variant, range=Optional[Union[str, AlleleId]])
