// ATTN: Replace me
const jwt = '';
const headers = {
    'Authorization': 'Bearer ' + jwt,
};

const baseUrl = 'https://interop-platform-api-v1.east.zocdoccloud.com';

const softwaresToUpdate = new Set([
    '01HATYKNQF82R0HCX3E6HBJKYM', // ECloud Pro
])

const fetchAllSoftware = async () => {
    const result = await fetch(baseUrl + '/interop-platform-api/v1/internal/software', {
        method: 'GET',
        headers,
    });

    if (result.status != 200) {
        throw new Error('Get all software failed. Status: ' + result.status)
    }

    const res = await result.json()

    return res.software_list;
}

const getSoftware = async (softwareId) => {
    const result = await fetch(baseUrl + '/interop-platform-api/v1/internal/software/' + softwareId, {
        method: 'GET',
        headers,
    });

    if (result.status != 200) {
        throw new Error(`Get software ${softwareId} failed. Status: ${result.status}`)
    }

    return await result.json();
}

const updateSoftware = async (softwareId, software) => {
    const result = await fetch(baseUrl + '/interop-platform-api/v1/internal/software/' + softwareId, {
        method: 'PUT',
        headers: {
            'Authorization': 'Bearer ' + jwt,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(software)
    });

    if (result.status !== 200) {
        const errorBody = await result.text();
        throw new Error(`Update software ${softwareId} failed. Status: ${result.status}, Response: ${errorBody}`);
    }
}

const updateSoftwareHello = async (softwareId) => {
    const software = await getSoftware(softwareId);

    console.log(`Updating software ${softwareId} (${software.name})`)

    await updateSoftware(softwareId, software);

    const software1Updated = await getSoftware(softwareId);

    console.log(`Software ${softwareId} (${software.name}) updated.`)
};

const runProgram = async () => {
    const softwareList = await fetchAllSoftware();

    for (const software of softwareList) {
        if (softwaresToUpdate.has(software.software_id)) {
            await updateSoftwareHello(software.software_id);
        }
    }
}

runProgram()
