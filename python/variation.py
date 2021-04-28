# Auto generated from variation.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-28 15:35
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
from . allele import Allele
from . core import BiologicalSequence, GeneCurie, TranscriptCurie
from . reference import ReferenceCurie
from linkml.utils.metamodelcore import URIorCURIE, XSDDate
from linkml_model.types import Date, String, Uriorcurie

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
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/variation/')


# Types

# Class references
class VariantCurie(URIorCURIE):
    pass


@dataclass
class Variant(YAMLRoot):
    """
    A DNA sequence that differs relative to a designated reference sequence. The sequence occurs at a single position
    or in contiguous nucleotides.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variation/Variant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variation/Variant")

    curie: Union[str, VariantCurie] = None
    hgvs_nomenclature: Optional[str] = None
    genomic_reference_sequence: Optional[Union[str, BiologicalSequence]] = None
    genomic_variant_sequence: Optional[Union[str, BiologicalSequence]] = None
    padding_left: Optional[Union[str, BiologicalSequence]] = None
    padding_right: Optional[Union[str, BiologicalSequence]] = None
    date_produced: Optional[Union[str, XSDDate]] = None
    release: Optional[str] = None
    data_provider: Optional[Union[str, List[str]]] = empty_list()
    computed_gene: Optional[Union[str, GeneCurie]] = None
    variant_of_transcript: Optional[Union[str, TranscriptCurie]] = None
    variant_of_allele: Optional[Union[dict, Allele]] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    type: Optional[Union[str, URIorCURIE]] = None
    references: Optional[Union[Union[str, ReferenceCurie], List[Union[str, ReferenceCurie]]]] = empty_list()
    notes: Optional[Union[str, List[str]]] = empty_list()
    protein_sequence: Optional[Union[str, BiologicalSequence]] = None
    cross_references: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is None:
            raise ValueError("curie must be supplied")
        if not isinstance(self.curie, VariantCurie):
            self.curie = VariantCurie(self.curie)

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

        if self.computed_gene is not None and not isinstance(self.computed_gene, GeneCurie):
            self.computed_gene = GeneCurie(self.computed_gene)

        if self.variant_of_transcript is not None and not isinstance(self.variant_of_transcript, TranscriptCurie):
            self.variant_of_transcript = TranscriptCurie(self.variant_of_transcript)

        if self.variant_of_allele is not None and not isinstance(self.variant_of_allele, Allele):
            self.variant_of_allele = Allele(**self.variant_of_allele)

        if self.synonyms is None:
            self.synonyms = []
        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms]
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.type is not None and not isinstance(self.type, URIorCURIE):
            self.type = URIorCURIE(self.type)

        if self.references is None:
            self.references = []
        if not isinstance(self.references, list):
            self.references = [self.references]
        self.references = [v if isinstance(v, ReferenceCurie) else ReferenceCurie(v) for v in self.references]

        if self.notes is None:
            self.notes = []
        if not isinstance(self.notes, list):
            self.notes = [self.notes]
        self.notes = [v if isinstance(v, str) else str(v) for v in self.notes]

        if self.protein_sequence is not None and not isinstance(self.protein_sequence, BiologicalSequence):
            self.protein_sequence = BiologicalSequence(self.protein_sequence)

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

slots.notes = Slot(uri=DEFAULT_.notes, name="notes", curie=DEFAULT_.curie('notes'),
                   model_uri=DEFAULT_.notes, domain=None, range=Optional[Union[str, List[str]]])

slots.hgvs_nomenclature = Slot(uri=DEFAULT_.hgvs_nomenclature, name="hgvs_nomenclature", curie=DEFAULT_.curie('hgvs_nomenclature'),
                   model_uri=DEFAULT_.hgvs_nomenclature, domain=Variant, range=Optional[str])

slots.genomic_reference_sequence = Slot(uri=DEFAULT_.genomic_reference_sequence, name="genomic_reference_sequence", curie=DEFAULT_.curie('genomic_reference_sequence'),
                   model_uri=DEFAULT_.genomic_reference_sequence, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.genomic_variant_sequence = Slot(uri=DEFAULT_.genomic_variant_sequence, name="genomic_variant_sequence", curie=DEFAULT_.curie('genomic_variant_sequence'),
                   model_uri=DEFAULT_.genomic_variant_sequence, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.padding_left = Slot(uri=DEFAULT_.padding_left, name="padding_left", curie=DEFAULT_.curie('padding_left'),
                   model_uri=DEFAULT_.padding_left, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.padding_right = Slot(uri=DEFAULT_.padding_right, name="padding_right", curie=DEFAULT_.curie('padding_right'),
                   model_uri=DEFAULT_.padding_right, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.protein_sequence = Slot(uri=DEFAULT_.protein_sequence, name="protein_sequence", curie=DEFAULT_.curie('protein_sequence'),
                   model_uri=DEFAULT_.protein_sequence, domain=Variant, range=Optional[Union[str, BiologicalSequence]])

slots.computed_gene = Slot(uri=DEFAULT_.computed_gene, name="computed_gene", curie=DEFAULT_.curie('computed_gene'),
                   model_uri=DEFAULT_.computed_gene, domain=Variant, range=Optional[Union[str, GeneCurie]])

slots.variant_of_transcript = Slot(uri=DEFAULT_.variant_of_transcript, name="variant_of_transcript", curie=DEFAULT_.curie('variant_of_transcript'),
                   model_uri=DEFAULT_.variant_of_transcript, domain=Variant, range=Optional[Union[str, TranscriptCurie]])

slots.variant_of_allele = Slot(uri=DEFAULT_.variant_of_allele, name="variant_of_allele", curie=DEFAULT_.curie('variant_of_allele'),
                   model_uri=DEFAULT_.variant_of_allele, domain=Variant, range=Optional[Union[dict, Allele]])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])
