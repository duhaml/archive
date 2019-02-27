import React from 'react'
import { StyleSheet, View, TextInput, Button, Text } from 'react-native'

class Tutorial extends React.Component {
  render() {
    return (
        <View style={{marginTop: 150}}>
            <Text>Ceci est un tuto du Q</Text>
            <Button title="Ok, jai tout compris !" onPress={() => {this.props.navigation.navigate("GlobalMarketView")}}/>
        </View>
    )
  }
}

export default Tutorial
