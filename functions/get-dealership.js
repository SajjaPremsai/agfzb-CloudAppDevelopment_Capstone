const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const Cloudant = require('@cloudant/cloudant');

// Initialize Cloudant connection with IAM authentication
async function dbCloudantConnect() {
    try {
        const cloudant = Cloudant({
            plugins: { iamauth: { iamApiKey: 'NzfXNIB_O7o4ozaVk1TWRKvvqQL7w4K1gm5L-Df38Zv2' } }, // Replace with your IAM API key
            url: 'https://1019b037-d6c8-437c-bdca-d8f02dd27dd5-bluemix.cloudantnosqldb.appdomain.cloud', // Replace with your Cloudant URL
        });

        const db = cloudant.use('dealerships');
        console.info('Connect success! Connected to DB');
        return db;
    } catch (err) {
        console.error('Connect failure: ' + err.message + ' for Cloudant DB');
        throw err;
    }
}

let db;

(async () => {
    db = await dbCloudantConnect();
})();

app.use(express.json());

// Define a route to get all dealerships with optional state and ID filters
app.get('/dealerships/get', (req, res) => {
    const { state, id } = req.query;

    // Create a selector object based on query parameters
    const selector = {};
    if (state) {
        selector.state = state;
    }

    if (id) {
        selector.id = parseInt(id); // Filter by "id" with a value of 1
    }

    const queryOptions = {
        selector,
        limit: 10, // Limit the number of documents returned to 10
    };

    db.find(queryOptions, (err, body) => {
        if (err) {
            console.error('Error fetching dealerships:', err);
            res.status(500).json({ error: 'An error occurred while fetching dealerships.' });
        } else {
            const dealerships = body.docs;
            res.json(dealerships);
        }
    });
});


// Define a route to get a dealership by ID
app.get('/dealerships/:id', (req, res) => {
    const dealershipId = parseInt(req.params.id);

    if (isNaN(dealershipId)) {
        return res.status(400).json({ error: 'Invalid dealership ID' });
    }

    const queryOptions = {
        selector: {
            id: dealershipId,
        },
        limit: 1, // Limit to one document as the ID should be unique
    };

    db.find(queryOptions, (err, body) => {
        if (err) {
            console.error('Error fetching dealership by ID:', err);
            res.status(500).json({ error: 'An error occurred while fetching dealership by ID.' });
        } else {
            const dealership = body.docs[0];
            if (dealership) {
                res.json(dealership);
            } else {
                res.status(404).json({ error: 'Dealership not found' });
            }
        }
    });
});

app.get('/dealerships/state/:state', (req, res) => {
    const dealershipState = req.params.state; // Note: The state parameter is a string, not an integer

    const queryOptions = {
        selector: {
            state: dealershipState,
        },
        limit: 1, // Limit to one document as the ID should be unique
    };

    db.find(queryOptions, (err, body) => {
        if (err) {
            console.error('Error fetching dealership by state:', err);
            res.status(500).json({ error: 'An error occurred while fetching dealership by state.' });
        } else {
            const dealership = body.docs[0];
            if (dealership) {
                res.json(dealership);
            } else {
                res.status(404).json({ error: 'Dealership not found' });
            }
        }
    });
});



app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});