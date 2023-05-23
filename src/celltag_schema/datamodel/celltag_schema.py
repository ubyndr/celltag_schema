# Auto generated from celltag_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-05-23T11:24:31
# Schema: CxG_meta-schema
#
# id: https://w3id.org/scFAIR/celltag_schema
# description: A meta-schema that records connections, types, provenance and evidence for the obs fields in the CZI CxG standard
# license: Apache Software License 2.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CELLTAG_SCHEMA = CurieNamespace('celltag_schema', 'https://w3id.org/scFAIR/celltag_schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CELLTAG_SCHEMA


# Types

# Class references



@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.Container
    class_class_curie: ClassVar[str] = "celltag_schema:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.Container

    meta: Optional[Union[Union[dict, "CxGMetaSchema"], List[Union[dict, "CxGMetaSchema"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.meta, list):
            self.meta = [self.meta] if self.meta is not None else []
        self.meta = [v if isinstance(v, CxGMetaSchema) else CxGMetaSchema(**as_dict(v)) for v in self.meta]

        super().__post_init__(**kwargs)


@dataclass
class CxGMetaSchema(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.CxGMetaSchema
    class_class_curie: ClassVar[str] = "celltag_schema:CxGMetaSchema"
    class_name: ClassVar[str] = "CxGMetaSchema"
    class_model_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.CxGMetaSchema

    field_name: str = None
    field_type: Union[str, "FieldTypeEnum"] = None
    field_scope: Optional[Union[str, "FieldScopeEnum"]] = None
    field_relationship: Optional[Union[Union[dict, "FieldRelationship"], List[Union[dict, "FieldRelationship"]]]] = empty_list()
    manual_annotation_metadata: Optional[Union[dict, "ManualAnnotationMetadata"]] = None
    automated_cell_type_annotation_metadata: Optional[Union[dict, "AutomatedCellTypeAnnotationMetadata"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.field_name):
            self.MissingRequiredField("field_name")
        if not isinstance(self.field_name, str):
            self.field_name = str(self.field_name)

        if self._is_empty(self.field_type):
            self.MissingRequiredField("field_type")
        if not isinstance(self.field_type, FieldTypeEnum):
            self.field_type = FieldTypeEnum(self.field_type)

        if self.field_scope is not None and not isinstance(self.field_scope, FieldScopeEnum):
            self.field_scope = FieldScopeEnum(self.field_scope)

        if not isinstance(self.field_relationship, list):
            self.field_relationship = [self.field_relationship] if self.field_relationship is not None else []
        self.field_relationship = [v if isinstance(v, FieldRelationship) else FieldRelationship(**as_dict(v)) for v in self.field_relationship]

        if self.manual_annotation_metadata is not None and not isinstance(self.manual_annotation_metadata, ManualAnnotationMetadata):
            self.manual_annotation_metadata = ManualAnnotationMetadata(**as_dict(self.manual_annotation_metadata))

        if self.automated_cell_type_annotation_metadata is not None and not isinstance(self.automated_cell_type_annotation_metadata, AutomatedCellTypeAnnotationMetadata):
            self.automated_cell_type_annotation_metadata = AutomatedCellTypeAnnotationMetadata(**as_dict(self.automated_cell_type_annotation_metadata))

        super().__post_init__(**kwargs)


@dataclass
class FieldRelationship(YAMLRoot):
    """
    Relationship between fields
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.FieldRelationship
    class_class_curie: ClassVar[str] = "celltag_schema:FieldRelationship"
    class_name: ClassVar[str] = "FieldRelationship"
    class_model_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.FieldRelationship

    relation: Union[str, "RelationEnum"] = None
    object: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        if not isinstance(self.relation, RelationEnum):
            self.relation = RelationEnum(self.relation)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ManualAnnotationMetadata(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.ManualAnnotationMetadata
    class_class_curie: ClassVar[str] = "celltag_schema:ManualAnnotationMetadata"
    class_name: ClassVar[str] = "ManualAnnotationMetadata"
    class_model_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.ManualAnnotationMetadata

    author: Optional[str] = None
    supporting_publication: Optional[str] = None
    evidence_comment: Optional[str] = None
    marker_evidence: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.author is not None and not isinstance(self.author, str):
            self.author = str(self.author)

        if self.supporting_publication is not None and not isinstance(self.supporting_publication, str):
            self.supporting_publication = str(self.supporting_publication)

        if self.evidence_comment is not None and not isinstance(self.evidence_comment, str):
            self.evidence_comment = str(self.evidence_comment)

        if not isinstance(self.marker_evidence, list):
            self.marker_evidence = [self.marker_evidence] if self.marker_evidence is not None else []
        self.marker_evidence = [v if isinstance(v, str) else str(v) for v in self.marker_evidence]

        super().__post_init__(**kwargs)


@dataclass
class AutomatedCellTypeAnnotationMetadata(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.AutomatedCellTypeAnnotationMetadata
    class_class_curie: ClassVar[str] = "celltag_schema:AutomatedCellTypeAnnotationMetadata"
    class_name: ClassVar[str] = "AutomatedCellTypeAnnotationMetadata"
    class_model_uri: ClassVar[URIRef] = CELLTAG_SCHEMA.AutomatedCellTypeAnnotationMetadata

    algorithm: Optional[str] = None
    algorithm_reference: Optional[str] = None
    reference_data: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.algorithm is not None and not isinstance(self.algorithm, str):
            self.algorithm = str(self.algorithm)

        if self.algorithm_reference is not None and not isinstance(self.algorithm_reference, str):
            self.algorithm_reference = str(self.algorithm_reference)

        if self.reference_data is not None and not isinstance(self.reference_data, str):
            self.reference_data = str(self.reference_data)

        super().__post_init__(**kwargs)


# Enumerations
class RelationEnum(EnumDefinitionImpl):

    broader_than = PermissibleValue(text="broader_than")

    _defn = EnumDefinition(
        name="RelationEnum",
    )

class FieldTypeEnum(EnumDefinitionImpl):

    cell_type_ontology_label = PermissibleValue(text="cell_type_ontology_label")
    cell_type_ontology_id = PermissibleValue(text="cell_type_ontology_id")
    free_text_cell_type_name = PermissibleValue(text="free_text_cell_type_name")

    _defn = EnumDefinition(
        name="FieldTypeEnum",
    )

class FieldScopeEnum(EnumDefinitionImpl):

    exact = PermissibleValue(text="exact")
    broad = PermissibleValue(text="broad")

    _defn = EnumDefinition(
        name="FieldScopeEnum",
    )

# Slots
class slots:
    pass

slots.container__meta = Slot(uri=CELLTAG_SCHEMA.meta, name="container__meta", curie=CELLTAG_SCHEMA.curie('meta'),
                   model_uri=CELLTAG_SCHEMA.container__meta, domain=None, range=Optional[Union[Union[dict, CxGMetaSchema], List[Union[dict, CxGMetaSchema]]]])

slots.cxGMetaSchema__field_name = Slot(uri=CELLTAG_SCHEMA.field_name, name="cxGMetaSchema__field_name", curie=CELLTAG_SCHEMA.curie('field_name'),
                   model_uri=CELLTAG_SCHEMA.cxGMetaSchema__field_name, domain=None, range=str)

slots.cxGMetaSchema__field_type = Slot(uri=CELLTAG_SCHEMA.field_type, name="cxGMetaSchema__field_type", curie=CELLTAG_SCHEMA.curie('field_type'),
                   model_uri=CELLTAG_SCHEMA.cxGMetaSchema__field_type, domain=None, range=Union[str, "FieldTypeEnum"])

slots.cxGMetaSchema__field_scope = Slot(uri=CELLTAG_SCHEMA.field_scope, name="cxGMetaSchema__field_scope", curie=CELLTAG_SCHEMA.curie('field_scope'),
                   model_uri=CELLTAG_SCHEMA.cxGMetaSchema__field_scope, domain=None, range=Optional[Union[str, "FieldScopeEnum"]])

slots.cxGMetaSchema__field_relationship = Slot(uri=CELLTAG_SCHEMA.field_relationship, name="cxGMetaSchema__field_relationship", curie=CELLTAG_SCHEMA.curie('field_relationship'),
                   model_uri=CELLTAG_SCHEMA.cxGMetaSchema__field_relationship, domain=None, range=Optional[Union[Union[dict, FieldRelationship], List[Union[dict, FieldRelationship]]]])

slots.cxGMetaSchema__manual_annotation_metadata = Slot(uri=CELLTAG_SCHEMA.manual_annotation_metadata, name="cxGMetaSchema__manual_annotation_metadata", curie=CELLTAG_SCHEMA.curie('manual_annotation_metadata'),
                   model_uri=CELLTAG_SCHEMA.cxGMetaSchema__manual_annotation_metadata, domain=None, range=Optional[Union[dict, ManualAnnotationMetadata]])

slots.cxGMetaSchema__automated_cell_type_annotation_metadata = Slot(uri=CELLTAG_SCHEMA.automated_cell_type_annotation_metadata, name="cxGMetaSchema__automated_cell_type_annotation_metadata", curie=CELLTAG_SCHEMA.curie('automated_cell_type_annotation_metadata'),
                   model_uri=CELLTAG_SCHEMA.cxGMetaSchema__automated_cell_type_annotation_metadata, domain=None, range=Optional[Union[dict, AutomatedCellTypeAnnotationMetadata]])

slots.fieldRelationship__relation = Slot(uri=CELLTAG_SCHEMA.relation, name="fieldRelationship__relation", curie=CELLTAG_SCHEMA.curie('relation'),
                   model_uri=CELLTAG_SCHEMA.fieldRelationship__relation, domain=None, range=Union[str, "RelationEnum"])

slots.fieldRelationship__object = Slot(uri=CELLTAG_SCHEMA.object, name="fieldRelationship__object", curie=CELLTAG_SCHEMA.curie('object'),
                   model_uri=CELLTAG_SCHEMA.fieldRelationship__object, domain=None, range=str)

slots.manualAnnotationMetadata__author = Slot(uri=CELLTAG_SCHEMA.author, name="manualAnnotationMetadata__author", curie=CELLTAG_SCHEMA.curie('author'),
                   model_uri=CELLTAG_SCHEMA.manualAnnotationMetadata__author, domain=None, range=Optional[str])

slots.manualAnnotationMetadata__supporting_publication = Slot(uri=CELLTAG_SCHEMA.supporting_publication, name="manualAnnotationMetadata__supporting_publication", curie=CELLTAG_SCHEMA.curie('supporting_publication'),
                   model_uri=CELLTAG_SCHEMA.manualAnnotationMetadata__supporting_publication, domain=None, range=Optional[str])

slots.manualAnnotationMetadata__evidence_comment = Slot(uri=CELLTAG_SCHEMA.evidence_comment, name="manualAnnotationMetadata__evidence_comment", curie=CELLTAG_SCHEMA.curie('evidence_comment'),
                   model_uri=CELLTAG_SCHEMA.manualAnnotationMetadata__evidence_comment, domain=None, range=Optional[str])

slots.manualAnnotationMetadata__marker_evidence = Slot(uri=CELLTAG_SCHEMA.marker_evidence, name="manualAnnotationMetadata__marker_evidence", curie=CELLTAG_SCHEMA.curie('marker_evidence'),
                   model_uri=CELLTAG_SCHEMA.manualAnnotationMetadata__marker_evidence, domain=None, range=Optional[Union[str, List[str]]])

slots.automatedCellTypeAnnotationMetadata__algorithm = Slot(uri=CELLTAG_SCHEMA.algorithm, name="automatedCellTypeAnnotationMetadata__algorithm", curie=CELLTAG_SCHEMA.curie('algorithm'),
                   model_uri=CELLTAG_SCHEMA.automatedCellTypeAnnotationMetadata__algorithm, domain=None, range=Optional[str])

slots.automatedCellTypeAnnotationMetadata__algorithm_reference = Slot(uri=CELLTAG_SCHEMA.algorithm_reference, name="automatedCellTypeAnnotationMetadata__algorithm_reference", curie=CELLTAG_SCHEMA.curie('algorithm_reference'),
                   model_uri=CELLTAG_SCHEMA.automatedCellTypeAnnotationMetadata__algorithm_reference, domain=None, range=Optional[str])

slots.automatedCellTypeAnnotationMetadata__reference_data = Slot(uri=CELLTAG_SCHEMA.reference_data, name="automatedCellTypeAnnotationMetadata__reference_data", curie=CELLTAG_SCHEMA.curie('reference_data'),
                   model_uri=CELLTAG_SCHEMA.automatedCellTypeAnnotationMetadata__reference_data, domain=None, range=Optional[str])