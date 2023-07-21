from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Session(BaseModel):
    """
    Represents a session object with a unique identifier, metadata,
    and other attributes.

    Attributes
    ----------
    uuid : Optional[str]
        A unique identifier for the session.
        This is generated server-side and is not expected to be present on creation.
    created_at : str
        The timestamp when the session was created.
        Generated by the server.
    updated_at : str
        The timestamp when the session was last updated.
        Generated by the server.
    deleted_at : Optional[datetime]
        The timestamp when the session was deleted.
        Generated by the server.
    session_id : str
        The unique identifier of the session.
    metadata : Dict[str, Any]
        The metadata associated with the session.
    """

    uuid: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
    session_id: str
    metadata: Dict[str, Any]


class Summary(BaseModel):
    """
    Represents a summary of a conversation.

    Attributes
    ----------
    uuid : str
        The unique identifier of the summary.
    created_at : str
        The timestamp of when the summary was created.
    content : str
        The content of the summary.
    recent_message_uuid : str
        The unique identifier of the most recent message in the conversation.
    token_count : int
        The number of tokens in the summary.

    Methods
    -------
    to_dict() -> Dict[str, Any]:
        Returns a dictionary representation of the summary.
    """

    uuid: str = Field("A uuid is required")
    created_at: str = Field("A created_at is required")
    content: str = Field("Content is required")
    recent_message_uuid: str = Field("A recent_message_uuid is required")
    token_count: int = Field("A token_count is required")

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the summary.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the summary.
        """
        return self.dict()


class Message(BaseModel):
    """
    Represents a message in a conversation.

    Attributes
    ----------
    uuid : str, optional
        The unique identifier of the message.
    created_at : str, optional
        The timestamp of when the message was created.
    role : str
        The role of the sender of the message (e.g., "user", "assistant").
    content : str
        The content of the message.
    token_count : int, optional
        The number of tokens in the message.

    Methods
    -------
    to_dict() -> Dict[str, Any]:
        Returns a dictionary representation of the message.
    """

    role: str = Field("A role is required")
    content: str = Field("Content is required")
    uuid: Optional[str] = Field(optional=True, default=None)
    created_at: Optional[str] = Field(optional=True, default=None)
    token_count: Optional[int] = Field(optional=True, default=None)
    metadata: Optional[Dict[str, Any]] = Field(optional=True, default=None)

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the message.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the message.
        """
        return self.dict()


class Memory(BaseModel):
    """
    Represents a memory object with messages, metadata, and other attributes.

    Attributes
    ----------
    messages : Optional[List[Dict[str, Any]]]
        A list of message objects, where each message contains a role and content.
    metadata : Optional[Dict[str, Any]]
        A dictionary containing metadata associated with the memory.
    summary : Optional[Summary]
        A Summary object.
    uuid : Optional[str]
        A unique identifier for the memory.
    created_at : Optional[str]
        The timestamp when the memory was created.
    token_count : Optional[int]
        The token count of the memory.

    Methods
    -------
    to_dict() -> Dict[str, Any]:
        Returns a dictionary representation of the message.
    """

    messages: List[Message] = Field(
        default=[], description="A List of Messages or empty List is required"
    )
    metadata: Optional[Dict[str, Any]] = Field(optional=True, default=None)
    summary: Optional[Summary] = Field(optional=True, default=None)
    uuid: Optional[str] = Field(optional=True, default=None)
    created_at: Optional[str] = Field(optional=True, default=None)
    token_count: Optional[int] = Field(optional=True, default=None)

    def to_dict(self) -> Dict[str, Any]:
        return self.dict()


class MemorySearchPayload(BaseModel):
    """
    Represents a search payload for querying memory.

    Attributes
    ----------
    metadata : Dict[str, Any]
        Metadata associated with the search query.
    text : str
        The text of the search query.
    """

    text: str = Field("A text is required")
    metadata: Optional[Dict[str, Any]] = Field(optional=True, default=None)


class MemorySearchResult(BaseModel):
    """
    Represents a search result from querying memory.

    Attributes
    ----------
    message : Optional[Dict[str, Any]]
        The message associated with the search result.
    metadata : Optional[Dict[str, Any]]
        Metadata associated with the search result.
    summary : Optional[str]
        The summary of the search result.
    dist : Optional[float]
        The distance metric of the search result.
    """

    message: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    summary: Optional[str] = None
    dist: Optional[float] = None


class Document(BaseModel):
    """
    Represents a document base.

    Attributes
    ----------
    uuid : Optional[str]
        The unique identifier of the document.
    created_at : Optional[datetime]
        The timestamp of when the document was created.
    updated_at : Optional[datetime]
        The timestamp of when the document was last updated.
    deleted_at : Optional[datetime]
        The timestamp of when the document was deleted.
    document_id : Optional[str]
        The unique identifier of the document (name or some id).
    content : str
        The content of the document.
    metadata : Optional[Dict[str, Any]]
        Any additional metadata associated with the document.
    embedding : Optional[List[float]]
        The embedding of the document.
    """

    uuid: Optional[str] = None
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
    document_id: Optional[str]
    content: Optional[str]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    embedding: Optional[List[float]]

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the document.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the document.
        """
        return self.dict()


class DocumentCollection(BaseModel):
    """
    Represents a collection of documents.

    Attributes
    ----------
    uuid : UUID
        The unique identifier of the document collection.
    created_at : datetime
        The timestamp of when the document collection was created.
    updated_at : datetime
        The timestamp of when the document collection was last updated.
    deleted_at : datetime
        The timestamp of when the document collection was deleted.
    id : str
        The name or id of the document collection.
    description : str
        The description of the document collection.
    metadata : Optional[Dict[str, Any]]
        Any additional metadata associated with the document collection.
    embedding_model_name : Optional[str]
        The name of the embedding model.
    embedding_dimensions : int
        The dimensions of the embedding model.
    distance_function : Optional[str]
        The distance function used in the model.
    is_normalized : Optional[bool]
        Flag to check if the model is normalized.
    documents: List[Document] = Field(
        default=[], description="A List of Documents or empty List"
    )
    """

    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
    name: str
    description: Optional[str]
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    embedding_model_name: Optional[str]
    embedding_dimensions: Optional[int]
    distance_function: Optional[str]
    is_normalized: Optional[bool]

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the document collection.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the document collection.
        """
        return self.dict()
