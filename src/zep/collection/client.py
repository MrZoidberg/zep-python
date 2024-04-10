# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.document_collection_response import DocumentCollectionResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CollectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.List[DocumentCollectionResponse]]:
        """
        Returns a list of all DocumentCollections.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.collection.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "collections"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[typing.List[DocumentCollectionResponse]], _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, collection_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentCollectionResponse:
        """
        Returns a DocumentCollection if it exists.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.collection.get(
            collection_name="collectionName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(DocumentCollectionResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        collection_name: str,
        *,
        description: typing.Optional[str] = OMIT,
        embedding_dimensions: int,
        is_auto_embedded: bool,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        If a collection with the same name already exists, an error will be returned.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - description: typing.Optional[str].

            - embedding_dimensions: int.

            - is_auto_embedded: bool. these needs to be pointers so that we can distinguish between false and unset when validating

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - name: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.collection.create(
            collection_name="collectionName",
            embedding_dimensions=1,
            is_auto_embedded=True,
            name="name",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "embedding_dimensions": embedding_dimensions,
            "is_auto_embedded": is_auto_embedded,
            "name": name,
        }
        if description is not OMIT:
            _request["description"] = description
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, collection_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If a collection with the same name already exists, it will be overwritten.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.collection.delete(
            collection_name="collectionName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        collection_name: str,
        *,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters:
            - collection_name: str. Name of the Document Collection

            - description: typing.Optional[str].

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.collection.update(
            collection_name="collectionName",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if description is not OMIT:
            _request["description"] = description
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def create_index(
        self,
        collection_name: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates an index for the specified DocumentCollection to improve query performance.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - force: typing.Optional[bool]. Force index creation, even if there are too few documents to index

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.collection.create_index(
            collection_name="collectionName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"collections/{jsonable_encoder(collection_name)}/index/create",
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "force": force,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCollectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.List[DocumentCollectionResponse]]:
        """
        Returns a list of all DocumentCollections.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.collection.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "collections"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[typing.List[DocumentCollectionResponse]], _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, collection_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentCollectionResponse:
        """
        Returns a DocumentCollection if it exists.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.collection.get(
            collection_name="collectionName",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(DocumentCollectionResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        collection_name: str,
        *,
        description: typing.Optional[str] = OMIT,
        embedding_dimensions: int,
        is_auto_embedded: bool,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        If a collection with the same name already exists, an error will be returned.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - description: typing.Optional[str].

            - embedding_dimensions: int.

            - is_auto_embedded: bool. these needs to be pointers so that we can distinguish between false and unset when validating

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - name: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.collection.create(
            collection_name="collectionName",
            embedding_dimensions=1,
            is_auto_embedded=True,
            name="name",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "embedding_dimensions": embedding_dimensions,
            "is_auto_embedded": is_auto_embedded,
            "name": name,
        }
        if description is not OMIT:
            _request["description"] = description
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, collection_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If a collection with the same name already exists, it will be overwritten.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.collection.delete(
            collection_name="collectionName",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        collection_name: str,
        *,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters:
            - collection_name: str. Name of the Document Collection

            - description: typing.Optional[str].

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.collection.update(
            collection_name="collectionName",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if description is not OMIT:
            _request["description"] = description
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{jsonable_encoder(collection_name)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def create_index(
        self,
        collection_name: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates an index for the specified DocumentCollection to improve query performance.

        Parameters:
            - collection_name: str. Name of the Document Collection

            - force: typing.Optional[bool]. Force index creation, even if there are too few documents to index

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from zep.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )
        await client.collection.create_index(
            collection_name="collectionName",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"collections/{jsonable_encoder(collection_name)}/index/create",
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "force": force,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)