@echo off
set DATABASE_URL=postgresql://postgres:123456@localhost:5432/casting_agency
set DATABASE_URL_TEST=postgresql://postgres:123456@localhost:5432/casting_agency_test
set ALGORITHMS=["RS256"]
set AUTH0_DOMAIN=dev-b1czbc11rvfxmip8.us.auth0.com
set API_AUDIENCE=casting
set AUTH0_CLIENT_ID=owpMku5G1kOmkS9nSt6PpnTXlgD84TL1
echo Environment variables set successfully!
