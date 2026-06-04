/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { HydroponicCreate } from '../models/HydroponicCreate';
import type { HydroponicListResponse } from '../models/HydroponicListResponse';
import type { HydroponicRead } from '../models/HydroponicRead';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class HydroponicsService {
    /**
     * List Hydroponic Data
     * @returns HydroponicListResponse Successful Response
     * @throws ApiError
     */
    public static listHydroponicDataHydroponicsGet(): CancelablePromise<HydroponicListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/hydroponics',
        });
    }
    /**
     * Create Hydroponic Data
     * @param requestBody
     * @returns HydroponicRead Successful Response
     * @throws ApiError
     */
    public static createHydroponicDataHydroponicsPost(
        requestBody: HydroponicCreate,
    ): CancelablePromise<HydroponicRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/hydroponics',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
